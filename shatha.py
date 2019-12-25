import mysql.connector

db = mysql.connector.connect(
  user='root',
  passwd='',
  host='localhost'
)
cursor = db.cursor()
cursor.execute('CREATE DATABASE board')
cursor.close()
db.close()

db = mysql.connector.connect(
  user='root',
  passwd='',
  host='localhost',
  database='board'
)



cursor = db.cursor()
cursor.execute('CREATE TABLE autistic (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255))')
cursor.close()
db.close()
