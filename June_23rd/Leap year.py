# Program for a Leap year with F-String

year = int(input("year :"))
if year%4==0:
    if year%100==0:
        if year%400==0:
            print(f"Year {year} is a Leap year")
        else:
            print(f"Year {year} is Not Leap year")
    else:
           print(f"Year {year} is a Leap year")
else:
    print(f"Year {year} is Not a Leap year")
    
