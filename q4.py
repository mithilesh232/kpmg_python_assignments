num=int(input("Enter the number"))
temp=num
rev=0

while(num>0):
    x=num%10
    rev=rev*10+x
    num=num//10
if (rev==temp):
    print("Yes.Given number is palindrome number")
else:
    print("No.Given number is not a palindrome number")
