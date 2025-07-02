'''Day = input("Enter the Day: ")
match Day:             
    case "Saturday":
        print("No Alarm")
    case "Sunday":
        print("No Alarm")
    case _:
        print("Alarm")'''

A1 = int(input("Enter 1st number: "))
A2 = int(input("Enter 2nd number: "))
A3 = int(input("Enter 3rd number: "))
if A1>0 and A2>0 and A3>0:
    cal=A1+A2+A3
    if cal!=180:
        print("This is value of Triangle : "+str(cal))
    else:
        pass
        
    
 
