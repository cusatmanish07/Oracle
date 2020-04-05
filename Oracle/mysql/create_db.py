import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  port=3303,
  user="root",
  passwd="root" 
  )

print(mydb)

mycursor = mydb.cursor()
mycursor.execute("CREATE DATABASE prod")

mycursor = mydb.cursor()
mycursor.execute("SHOW DATABASES")   

for x in mycursor:
 print(x)












