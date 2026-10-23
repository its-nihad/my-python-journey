#Count the numbers in a list which is greater than a given number

limit=25
nlst=[]
lst=[7,4,11,5,22,9,45,62,8,23,36,20,73,13,87,51,10,29,17]
for i in lst:
    if i>limit:
        nlst.append(i)

print(nlst)
print(len(nlst),"numbers are greater than",limit)