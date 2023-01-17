import mysql.connector

mydb=mysql.connector.connect(host="localhost",user="root",passwd="rps@123",database="kpmg")

mycursor=mydb.cursor()

mycursor.execute("create table product_info(productid  int,pname varchar(10),pdesc varchar(200))");
mycursor.execute("Insert into product_info values(123,'cap','covering head')");
mycursor.execute("Insert into product_info values(124,'pen','used for writing')");
mycursor.execute("Insert into product_info values(125,'bottle','keeping water'')");
mycursor.execute("Insert into product_info values(126,'phone','connecting with people')");
mycursor.execute("Insert into product_info values(127,'laptop','working with All the tasks')");
mycursor.execute("Select * from product_info");
mycursor.execute("Select * from product_info where productid='123'");

mydb.commit();