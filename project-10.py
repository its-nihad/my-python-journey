# simple calucator builted  with using python

num1=int(input("Enter the first number:"))
op=input("Type +,-,*,/ :")
num2=int(input("Enter the second number:"))
if op=="+":
    print(num1+num2)
elif op=="-":
    print(num1-num2)
elif op=="*":
    print(num1*num2)
elif op=="/":
    print(num1/num2)
else:
    print("Invalid Operator")
