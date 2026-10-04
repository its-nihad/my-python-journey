#sum of n numbers

data=int(input("Enter a N natural number:"))
s=0
for i in range(1,data+1,1):
    s=s+i
print("sum is:",s)