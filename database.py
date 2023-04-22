from sqlalchemy import create_engine, text

db_connection_string = "mysql+pymysql://0q7vq7ftm0fs4damnf6d:pscale_pw_RXvZNRVGx2ixvfZbhU70XerZVp1IXLquIbLOGu8eHS5@aws.connect.psdb.cloud/joviancareers?charset=utf8mb4"

engine = create_engine(db_connection_string,
                       connect_args={"ssl": {
                         "ssl_ca": "/etc/ssl/cert.pem"
                       }})

#with engine.connect() as conn:
#  result = conn.execute(text("select * from jobs"))
#  print(result.all())
#  result_dict = []
#  for row in result.all():
#    result_dict.append(dict(row))
#  print(result_dict)

def load_jobs_from_db():
  with engine.connect() as conn:
    result = conn.execute(text("select * from jobs"))
  jobs = []
  for row in result.all():
    #jobs.append(dict(row))
    jobs.append(row._mapping)
  return jobs