#check a string is symmetrical

word=input("Enter the word to check:")
l=int(len(word)/2)
h1=word[:l]
h2=word[l:]
if h1==h2:
    print("symmetrical")
else:
    print("not")