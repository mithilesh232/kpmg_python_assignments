import mysql.connector

mydb=mysql.connector.connect(host="localhost",user="root",passwd="rps@123",database="kpmg")

mycursor=mydb.cursor()

mycursor.execute("update kpmg_emps set ename='sandeep' where empid=123");

mydb.commit();