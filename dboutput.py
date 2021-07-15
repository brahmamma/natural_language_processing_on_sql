from ln2sql import ln2sql

import mysql.connector
con=pymysql.connector.connect(host="localhost",user="root",password="pavani@201")
cur=con.cursor()

def readfile(db_path):
    with open(db_path,'r') as sql_file:
        result=cur.execute(sql_file.read())
    con.commit()
    filename="Documents\ln2sql-master\output.txt"
    filep=open(filename,'r+')
    query=filep.read()
    cur.execute(query)
    records=cur.fetchall()
    for row in records:
        filep.write(row)
