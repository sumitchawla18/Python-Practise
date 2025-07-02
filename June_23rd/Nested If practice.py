age = int(input(" Age: "))
loyal = input (" Are you a loyal member,Select \"Y\" or \"N\" :").lower()
if age>=65 and loyal=="y":
    print ("20%")
elif age>=65 and loyal=="n":
    print ("10%")
elif age <65 and loyal=="y":
    print ("5%")
else:
    print ("No disc%")
