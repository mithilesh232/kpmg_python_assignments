import pickle
class Employee:
 def __init__(self,eno,ename,esal,eaddr):
    self.eno=eno;
    self.ename=ename;
    self.esal=esal;
    self.eaddr=eaddr;
 def display(self):
    print(self.eno,"\t",self.ename,"\t",self.esal,"\t",self.eaddr)

with open("employee.txt","wb") as f:
    e=Employee(130,"mahesh",10000,"banglore")
    pickle.dump(e,f)
    print("Pickling of Employee Object completed...")

with open("employee.txt","rb") as f:
    obj=pickle.load(f)
    print("Printing Employee Information after unpickling")
    obj.display()