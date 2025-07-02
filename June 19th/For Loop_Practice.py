# Len function only works on Strings and List
# Range is used to access indexes. First thing in Range is inclusive and 2nd is non inclusive

#numb = input("Enter the number :")
#len(numb)
#print(len(numb))

#now trying to run this without length function

'''length = 0
for i in numb:
    length+=1
print(length)'''

# Program for Factorial

ent = input("enter the number :")

fact = 1

for i in range(1,int(ent)+1):
    fact=fact*i
print(fact)
    
