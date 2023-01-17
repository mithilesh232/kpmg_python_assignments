addition=123 #global variable
def Adding(a, b):
    Sum = a + b #local variable Sum
    print(Sum)
def sub(a, b):
    sub = a - b #local variable Sum
    return sub
def message():
    print("am from default function")
Adding(3, 4)
print("After Calling the sub Function:",sub(3, 4))
message()