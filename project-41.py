#count the numbers of lowercase and uppercase characters in a string

lower=0
upper=0
sentance=input("Enter a sentance:")
for i in sentance:
    if i.islower():
        lower+=1
    elif i.isupper():
        upper+=1

print("lowercase characters:",lower)
print("uppercase characters:",upper)

