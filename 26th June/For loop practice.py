# Print numbers from 1 to 10

'''for i in range(1,11):
    print(i)'''

# Print squares of number from 1 to 5

'''for i in range(1,6):
    print(i*2)'''

# Print each character of the string

'''text = input("Enter any word: ")
for i in range(len(text)):
    print(text[i])'''

# Print ODD/Even numbers in the list. Also below program counts number of odd/even number in the list and sum of Even or Odd numbers

text = int (input("Enter any number: "))
even_c =0
odd_c=1
store=0

for i in range(1,text +1):
    
    #print("Range of the number is:",i)
    
    if i%2==0:
        print(f"This number {i} is Even")
        even_c +=1
        store =store + i          
    else:
        print(f"This number {i} is ODD")
        odd_c +=1

print("Total for Even number is",even_c)
print("Total ODD numbers in this range are",odd_c)
