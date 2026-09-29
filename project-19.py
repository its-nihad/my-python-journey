#To display multiplication table of any number

m=int(input("Enter the number to get multiplication table:"))
for num in range(1,11,1):
    print(num,"x",m,"=",num*m)