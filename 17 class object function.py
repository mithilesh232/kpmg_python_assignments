class Student:
	id=10
	name="hello"
	def __init__(self,sid):#constructor
		self.id=sid
	def __init__(self,sid,sname):#constructor
		self.id=sid
		self.name=sname
	def add(self,a,b):
		res=a+b
		print("sum of two numbers is : ",res)
	
		
s=Student(30,'raju')#calling ()

print(s.id)
print(s.name)
s.add(20,30)