def isEven(x):
    if x%2==0:
	    return True
    else: 
	    return False

list1=[0,2,4,3,5,6,9,10,30]		
l=list(filter(isEven,list1))
print(l)