import mysql.connector

mydb=mysql.connector.connect(host="localhost",user="root",passwd="rps@123",database="kpmg")

mycursor=mydb.cursor()

mycursor.execute("insert into kpmg_emps values(123,'suresh')");

mydb.commit();