class Employee:
	company = 'welcome to programming'#if there is no static keyword then it is instance var
	def __init__(self):# default constructor
		print('Hello World')
	def func_message(self):
		print('Welcome to Python Programming')
	def  addition(self,x,y):
		res=x+y
		print(res)
emp1 = Employee() # Created an Instance
print(emp1.company)
emp1.func_message()
emp1.addition(123,234);