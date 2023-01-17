class Calculator:
    def __init__(self):
        print("am from default constructor")
    def sayHello(self):
        print("am from super instance method")
    @classmethod
    def sayHi(cls,name):
        print("am from super class method"+name)
    @staticmethod
    def addition(a,b):
        print("am from static  method, addition is:",a+b)
Calculator.sayHi("accenture")   #way to call classmethod     
calc=Calculator()
calc.sayHello()
Calculator.addition(10,20)

class My_class:
    def sumofthree(self,a,b,c):
        print("sum of three numbers  :",a+b+c)

class Child(Calculator,My_class):
     def subofthree(self,a,b,c):
        print("sum of three numbers  :",a-b-c)
obj=Child()  
obj.sumofthree(2,3,4)
obj.addition(2,5)
obj.sayHello()
obj.sayHi("few are sleeping")    
obj.subofthree(10,12,13)