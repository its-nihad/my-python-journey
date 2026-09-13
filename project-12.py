#find the percentage and grades of marks of plustwo students(kerala)

mark=int(input("Enter the mark out of 1200:"))
p=mark/1200*100
print("percentage is:",p,"%")
if p>=90:
    print("Grade A+")
elif p>=80:
    print("Grade A")
elif p>=70:
    print("Grade B+")
elif p>=60:
    print("Grade B")
elif p>=50:
    print("Grade C+")
elif p>=40:
    print("Grade C")
elif p<=39:
    print("Failed")
