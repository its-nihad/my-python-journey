#check given number is a perfect number or not

num=int(input("Enter a number to check:"))
d=[]
for i in range(1,num):
    if num%i==0:
        d.append(i)
if sum(d)==num:
    print(num,"is a perfect number")
else:
    print(num,"is not a perfect number")
