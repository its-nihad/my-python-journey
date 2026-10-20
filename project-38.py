# To check a given year is leap year or not

year=int(input("Enter the year to check:"))
if year%4==0 and year%100!=0:
    print(year,"is a leap year")
else:
    print(year,"is not a leap year")