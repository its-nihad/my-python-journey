#display a pyramid shape using 12345 digits

for row in range(1,6):
    for col in range(1,row+1):
        print(col,end=" ")
    print()