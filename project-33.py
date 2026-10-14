#display a pyramid using alphabets(ABCDE)

n=65
for row in range(5):
    for col in range(row+1):
        print(chr(n),end=" ")
    print()
    n=n+1