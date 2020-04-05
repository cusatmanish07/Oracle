import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  port=3303,
  user="root",
  passwd="root",
  database="demo"
)

print(mydb)


