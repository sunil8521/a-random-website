import mysql.connector
import os

def database_connect(q):
  global dataBase,object
  dataBase = mysql.connector.connect(
        host=os.environ['host_key'],
        user=os.environ['admin_key'],
        passwd=os.environ['pass_key'],
        database='newdb'
)
  object = dataBase.cursor()
  query = q
  object.execute(query)
  myresult = object.fetchall()
  return myresult
  
def store():
  myresult=database_connect(q="select * from jobs")
  jobs_dict = []
  for row in myresult:
    job_dict = {}
    for index, value in enumerate(row):
      column_name = object.column_names[index]
      job_dict[column_name] = value
    jobs_dict.append(job_dict)
  dataBase.close()
  return jobs_dict

def by_id(i):
  myresult=database_connect(q=f"select * from jobs where id={i}")
  job_dict = {}
  for row in myresult:
    for index, value in enumerate(row):
      column_name = object.column_names[index]
      job_dict[column_name] = value
  dataBase.close()
  return job_dict
