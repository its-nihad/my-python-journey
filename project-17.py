#To find total number of alphabet,digits,vowels,and words in a given sentance

a=0
d=0
v=0
w=0
sentance=input("Enter a sentance:")
for char in sentance:
    if char.isalpha():
        a=a+1
    if char.isdigit():
        d=d+1
    if char in "aeiouAEIOU":
        v=v+1
    if char==" ":
        w=w+1
print("Number of alphabets in the sentance is:",a)
print("Number of digits in the sentance is:",d)
print("Number of vowels in the sentance is:",v)
print("Number of words in the sentance is:",w+1)