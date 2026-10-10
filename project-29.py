#even and odd counter

e=0
o=0
for num in range(1,51,1):
    if num%2==0:
        e=e+1
    elif num%2!=0:
        o=o+1
print("Total Even number is",e)
print("Total Odd number is",o)