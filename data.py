import mysql.connector
import os

def store():
    dataBase = mysql.connector.connect(
        host=os.environ['host_key'],
        user=os.environ['admin_key'],
        passwd=os.environ['pass_key'],
        database='newdb'
)
    object = dataBase.cursor()
    query = "select * from jobs"
    object.execute(query)
    myresult = object.fetchall()
    jobs_dict = []
    for row in myresult:
        job_dict = {}
        for index, value in enumerate(row):
            column_name = object.column_names[index]
            job_dict[column_name] = value
        jobs_dict.append(job_dict)
    dataBase.close()
    return jobs_dict

