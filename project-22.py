#case toggle/inverter

word=input("Enter a word or sentance:")
for char in word:
    if char.islower():
        print(char.upper(),end="")
    elif char.isupper():
        print(char.islower(),end="")