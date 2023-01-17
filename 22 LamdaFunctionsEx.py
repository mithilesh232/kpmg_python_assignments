# Anonymous functions / name less function
def my_fun(number):
    return number*number

#syntax: lambda args:expression

squareit=lambda n:n*n
print(squareit(34))
print(squareit(76))

addOfTwo=lambda a,b:a+b
print(addOfTwo(11,23))

bignumber=lambda a,b:a if a>b else b

print(bignumber(23,28))


#filter(function,sequence)