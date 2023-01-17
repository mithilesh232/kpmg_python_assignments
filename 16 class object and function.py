class Employee:
    company = 'welcome to programmin'
  
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender
		
    def func_message(self):
        print('Welcome to Python Programming')


emp1 = Employee('Mike', 25, 'Male') #()-->constructor calling

print(emp1.company)
emp1.func_message()
print(emp1.name)
print(emp1.age)
print(emp1.gender)