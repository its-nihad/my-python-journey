# find the electricity bill amount according to the unit consumed


'''
unit consumed       unit price
50 below            Rs. 3.35
51-100              Rs. 4.25
101-150             Rs. 5.35
151-200             Rs. 7.20
201-250             Rs. 8.50
'''

unit=float(input("Enter the unit consumed:"))
if unit<=50:
    print("Your  bill amount:",unit*3.35)
elif unit<=100 and unit>=51:
    print("Your  bill amount:", unit*4.25)
elif unit<=150 and unit>=101:
    print("Your  bill amount:", unit*5.35)
elif unit<=200 and unit>=151:
    print("Your  bill amount:", unit*7.20)
elif unit<=250 and unit>=201:
    print("Your  bill amount:", unit*8.50)

