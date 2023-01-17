#py -m pip install oracle
#py -m pip install mysql-connector  #mysql-connector-python latest 
import mysql.connector

mydb=mysql.connector.connect(host="localhost",user="root",passwd="rps@123",database="kpmg")

mycursor=mydb.cursor()

mycursor.execute("create table kpmg_emps(empid  int,ename varchar(10))");