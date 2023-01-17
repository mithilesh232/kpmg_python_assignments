import mysql.connector

mydb=mysql.connector.connect(host="localhost",user="root",passwd="rps@123",database="kpmg")

mycursor=mydb.cursor()
#mycursor.execute("create table products_info(productId int,productName varchar(50),productPrice int,productDesc varchar(300),productCategory varchar(100))")


class product:
    print("Product Management Application  \n 1.Add product  \n 2.Update Product \n 3. Delete ProductById \n 4. Get ProductById \n 5. Get All Products")
    x1=int(input("Enter the number"))
    if x1==1:
        mycursor.execute("Insert into products_info values(123,'cap',200,'covering head','clothes')");
        mycursor.execute("Insert into products_info values(124,'pen',100,'used for writing','study')");
        mycursor.execute("Insert into products_info values(125,'bottle',500,'keeping water','utensils')");
        mycursor.execute("Insert into products_info values(126,'phone',40000,'connecting with people','mobiles')");
        mycursor.execute("Insert into products_info values(127,'laptop',75000,'working with All the tasks','electronics')");
        mydb.commit()

    elif x1==2:
        pid = int(input("Enter product Id: "))
        pprice = input("Enter updated product price : ")
        mycursor.execute(f"UPDATE products_info set productPrice = {pprice}  where productId = {pid}")
        mydb.commit()
       

    elif x1==3:
        pid = int(input("Enter product Id for deleting: "))
        mycursor.execute(f"DELETE FROM products_info where productId = {pid}" )
        mydb.commit()

    elif x1==4:
        pid=int(input("Enter the product id:"))
        mycursor.execute(f"SELECT * FROM employees where productId={pid}")

        myresult = mycursor.fetchone()

        print(myresult)

    elif x1==5:

        mycursor.execute("select * from employees")
        data =mycursor.fetchall()

        for row in data:
            print("Employee Number:",row[0])
            print("Employee Name:",row[1])
            print("Employee Salary:",row[2])
            print("Employee Address:",row[3])
