import mysql.connector

mydb = mysql.connector.connect(
 host="localhost",
 port=3303,
 user="root",
 passwd="root",
 database="prod"
)

print(mydb)

#create table :
sql = "create table customer(name varchar(255), address varchar(255))"
#sql="insert into t1 values(1)"
mycursor = mydb.cursor()
mycursor.execute(sql)
mydb.commit()
print(mycursor.rowcount, "record inderted")
mycursor.execute("SHOW TABLES")
for x in mycursor:
 print(x)
#select statement :

mycursor.execute("select * from t1")
myresult = mycursor.fetchall()
for x in myresult:
 print(x)
mycursor.execute("select * from t1")
myresult = mycursor.fetchone()
for x in myresult:
 print(x)




