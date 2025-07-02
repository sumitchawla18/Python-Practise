# Program for a Leap year

year = int(input("year :"))
if year % 4 == 0 and year % 400 == 0:
    print("Leap")
elif year % 4 != 0:
    print("Not a leap year")


else:
    print("Leap year")
