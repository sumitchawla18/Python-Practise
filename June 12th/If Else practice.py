'''a = int(input("Please enter the Score :"))
if a>=90 and a<=100:
    print("Grade A")
elif a>=80 and a<=89:
    print("Grade B")
elif a>=70 and a<=79:
    print("Grade C")
elif a>=60 and a<=69:
    print("Grade D")
elif a<60:
    print("Grade F")'''
'''=======================================

a = int(input("Please enter the First Number : "))
b = int(input("Please enter the Second Number : "))
Opr = (input("Enter the Calculation : "))

if Opr=="+":
    print((a+b))
elif Opr=="-":
    print((a-b))   
elif Opr=="*":
    print((a*b))
elif Opr=="/":
    print((a/b))
#======================================================'''

'''Inp = input("Please enter the area you want to calculate(Circle,Rct or Sqr): ")
if Inp==(str("Circle")):
   pie =3.14
   rad =int(input("Please enter the radius: "))
   area = pie*rad*rad
   print(("area of the circle is: ")+str(area))
elif Inp==(str("Rct")):
    L1 =int(input("Enter the length: "))
    W1 =int(input("Enter the Width: "))
    area =L1*W1
    print(("area of the rect is: ")+str(area))
elif Inp==(str("Sqr")):
    S1 =int(input("Please Enter the Value Side: "))
    area = S1*S1
    print(("area of the Square is: ")+str(area))'''
#Inp = input("Enter the value: ")

C = input("Enter your selection in F or C: ")
if C==(str("C")):
   Cel =float(input("Enter the Temp Value in Celcius:")) 
   calc=Cel*9/5 + 32
   print(("Conversion of Celcius into Faren is : "+str(calc)))
elif C==(str("F")):
    Far =float(input("Enter the Temp Value in Faren:")) 
    calc=(Far-32)* 5/9
    print(("Conversion of Faren into Celcius is : "+str(calc)))



    
    
