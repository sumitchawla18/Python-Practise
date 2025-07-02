'''number = int(input("Enter the number here "))

if number%2==0:
    print("Number is Even")
else:
    print("Number is Odd")'''

number = int(input("Enter the number here "))

if number%2==0:
    print("Weird")
elif number%2!=0 and number<10:
    print("Not weird")
elif number%2!=0 and number>10 and number<30:
    print("weird")
elif number%2==0 and number>30:
    print("Not weird")

