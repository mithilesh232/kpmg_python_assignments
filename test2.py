class Invalidageexception(Exception):
 def __init__(self,message):
    print(message)
age=int(input("Enter your age"))
if age >= 18:
    print("You are eligiable to vote")
else:
    raise Invalidageexception('You are not allowed to vote')
