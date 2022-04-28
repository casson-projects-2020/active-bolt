import base64

def send_init( request ):
  """
  Args:
      request (flask.Request): HTTP request object.
  Returns:
      Code that will initialize a ipython notebook to be watched.
  """
  
  nbid = "nb_ID"
  if request.args and "nbid" in request.args:
    nbid = request.args.get( "nbid" )

  code = """

def avisa_instrutor( result ):
  import os

  url = 'https://us-central1-casson-pessoal.cloudfunctions.net/arki1_notebook'

  user = os.popen( "gcloud config get-value project" ).read().strip(" " + chr(10) + chr(13))

  code = base64.b64encode( result.info.raw_cell.encode( 'ascii' ))
  code = code.decode( 'ascii' )[-400:]

  params = { 'user': user, 'nb': 'nb_ID', 'ref': code }

  response = requests.get( url, params=params )
    
get_ipython().events.register('post_run_cell', avisa_instrutor )
"""

  code = code.replace( 'nb_ID', nbid )
  code = base64.b64encode( code.encode( 'ascii' ))
  code = code.decode( 'ascii' )

  return code





from google.cloud import bigquery

def ipython_watch( request ):
    """
        Args:
        request (flask.Request): HTTP request object.
    """

    bq_client = bigquery.Client()

    err = True

    if request.args:
        if "user" in request.args and "nb" in request.args and "ref" in request.args:
            err = False

            # if there are a new cell in a notebook, not registered yet, add it
            nb = "'" + request.args[ 'nb' ] + "'"
            ref = "'" + request.args[ 'ref' ] + "'"

            # this query will add a record in ipython_ref for the notebook if
            # the code does not already exist in the table, and will add it as
            # step 1 if no step exists, or max + 1 if we already have steps registered
            sql = """INSERT INTO `casson-pessoal.ipython_watch.ipython_ref`
                SELECT {nb}, {ref},
                        IFNULL(( SELECT  MAX( step ) + 1 
                                   FROM  `casson-pessoal.ipython_watch.ipython_ref`
                                  WHERE  nbid = {nb}), 1 ) 
                      FROM  
                            `bigquery-public-data.samples.gsod`
                     WHERE  0 = 
                            (SELECT COUNT( 1 ) FROM `casson-pessoal.ipython_watch.ipython_ref` 
                                            WHERE nbcode = {ref})
                     LIMIT  1 

            """.format( nb=nb, ref=ref )

            query_job = bq_client.query( sql )
            dummy = query_job.result()

            # now add the record of the execution of the cell
            user = "'" + request.args[ 'user' ] + "'"

            sql2 = """INSERT INTO `casson-pessoal.ipython_watch.ipython_data` 
                    SELECT CURRENT_DATE(), {user}, {nb},
                        ( SELECT step FROM `casson-pessoal.ipython_watch.ipython_ref`
                           WHERE nbid = {nb} AND nbcode = {ref}),
                           CURRENT_TIME()

                    """.format( user=user, nb=nb, ref=ref )

            query_job = bq_client.query( sql2 )
            dummy = query_job.result()

        else:
            sql = "INSERT INTO `casson-pessoal.ipython_watch.log` (log) VALUES( '"
            sql += 'ERRO: chamada com os valores-> '

            cont = 1
            for key, val in request.args.items():
                sql += key + ": " + val + " | "

                if cont > 10: break

    if err:
        sql += " HEADERS => "
        heads = [ id_.replace( "X-Appengine-", "" ) + ": " + request.headers[ id_ ] + " | "
                    for id_ in
                    [ "User-Agent", "X-Appengine-City",
                        "X-Appengine-Citylatlong",
                        "X-Appengine-Country",
                        "X-Appengine-User-Ip",
                        "X-Forwarded-For"
                    ]]
        sql += "".join( heads )

        query_job = bq_client.query( sql + "')" )
        dummy = query_job.result()

    return f'ok'
  
  
  
  
