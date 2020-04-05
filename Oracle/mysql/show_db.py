import mysql.connector

mydb = mysql.connector.connect(
 host="localhost",
 port=3303,
 user="root",
 passwd="root"
)

print(mydb)

mydbcursor = mydb.cursor()

mydbcursor.execute("SHOW DATABASES")
for x in mydbcursor: 
 print(x)

#mydbcursor.execute("CREATE USER 'nikki'@'localhost' IDENTIFIED BY 'nikki'")
mydbcursor.execute("select user, host from mysql.user")
for x in mydbcursor:
 print(x)




