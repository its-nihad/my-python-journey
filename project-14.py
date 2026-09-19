# To check whether the given word is palindrome

data=input("Enter the word:")
r=data[::-1]
if r==data:
    print("Is palindrome")
else:
    print("Not")
