import mysql.connector

def check(user,password):
  mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="root",
    database="attendance"
  )

  mycursor = mydb.cursor()

  mycursor.execute("SELECT user,pass,role FROM login")

  myresult = mycursor.fetchall()

  for x in myresult:
    if(x[0]==user and x[1]==password):
      return True
  return False