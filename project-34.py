#Display only even length words in a given string

word=[]
sentance=input("Enter a sentance:").split()
for words in sentance:
    if len(words)%2==0:
        word.append(words)
print(word)