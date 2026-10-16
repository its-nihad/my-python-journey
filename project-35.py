#find words which are greater than given length

word=[]
sentance=input("Enter a sentance:").split()
limit=int(input("Enter the limit of length of the word:"))
for words in sentance:
    if len(words)>limit:
        word.append(words)
print(word)