import mysql.connector

args={"host":"localhost","user":"root","password":"pavani@201"}
con=mysql.connector.connect(**args)
cur=con.cursor(dictionary=True)
def readtxt(path):
    
    with open(path,'r') as sql_file:
        result=cur.execute(sql_file.read(),multi=True)
    for res in result:
        pass
    
    con.commit()
    filename="output.txt"
    file=open(filename,'r')
    query=file.read()
    cur.execute(query)
    records=cur.fetchall()
    print(records)
    print(type(records))
    val=[]
    for row in records:
        print(row)
        for i in row.values():
            val.append(i)
            val.append(',')
    val.pop()
            
    return (query,val)


