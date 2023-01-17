class Employee:
	def __init__(self):
		self.eid=100
		self.ename='sandeep'
	def m1(self):
		self.address='india'
		print(self.eid)
emp=Employee()
emp.m1()
emp.salary=9000
print(emp.ename)
print(emp.__dict__)