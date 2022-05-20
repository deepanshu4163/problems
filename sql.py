import mysql.connector

mydb = mysql.connector.connect(
  host = "localhost",
  user = "testing",
  password = "",
  database = "classicmodels"
)

mycursor = mydb.cursor()

mycursor.execute("SELECT * FROM employees")

myresult = mycursor.fetchall()

for x in myresult:
  print(x)
