# to count the words in a sentance

sentance=input("Enter the sentance:")
c=0
for char in sentance:
    if char==" ":
        c=c+1
print("Total number of words = ",c+1)