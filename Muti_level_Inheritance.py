class MainClass:  #mutli-level inheritance
    def func_message(self):
        print('Welcome to Main Class')
 
class Child(MainClass):  # child class derived from MainClass
    def func_child(self):
        print('Welcome to Child Class')
        print('This class is inherited from Main Class') 
class ChildDerived(Child):#childDerived  From Child Class
 
    def func_Derived(self):
        print('Welcome to Derived Class')
        print('This class is inherited from Child Class')
         
print('------------')
chldev = ChildDerived()
chldev.func_Derived() 
print('------------')
chldev.func_child()
print('------------')
chldev.func_message()