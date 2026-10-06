#vowel counter

sentance=input("Enter a word or sentance:")
v=0
for vowel in sentance:
    if vowel in "aeiouAEIOU":
        v=v+1
        print(vowel,end=",")
print()
print("vowel count is:",v)

