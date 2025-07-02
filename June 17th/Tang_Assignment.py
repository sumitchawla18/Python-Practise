text = input("Please enter the String: ")
rev=""
for i in range(len(text)-1,-1,-1):
    rev +=text[i]
if rev==text:
    print ("This is palindrome")
else:
    print ("This is not palindrome")
        

'''text = input("Please enter the String: ")
rev = text[::-1]
if text==rev:
    print("Palin")
else:
    print("Not Palin")'''
    
            
