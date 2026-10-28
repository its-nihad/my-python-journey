# create tuple from an existing tuple. new tuple contains only the elements divisible by 3

tup1=(1,2,3,4,5,14,16,7,25,19,8,13,34,27,46,36)
lst=[]
for num in tup1:
    if num%3==0:
        lst.append(num)
tup2=tuple(lst)
print(tup2)
print(type(tup2))