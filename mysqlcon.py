import mysql.connector
def mysqlcon(mesaj):
    mydb = mysql.connector.connect(
     host="localhost",
     user="root",
     password="root",
     database="<DATABASE NAME HERE>",
      )
    list = []
    mycursor = mydb.cursor()

    mycursor.execute(mesaj)

    for i in mycursor:
        list.append(i)
    return list[0:20]
#mysqlcon(SELECT * FROM city")

