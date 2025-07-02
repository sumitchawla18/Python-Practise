#Every second character(a,r,n,B,l)
'''a="BajrangBali"
print(a[::2])'''

#Reverse string

'''a="BajrangBali"
print(a[::-1])'''

#First and last character (H,O)

'''b="Hello"
print(b[0:-1])'''

#Middle Characters (gra)

'''b="Programming"
print(b[3:6])'''

#Alternate Characters in Reverse (j,h,f,d,b)

'''text="abcdefghij"
print(text[::-2])'''

#Remove Vowels

'''text="Hello World"
i=0
print(text[i:i+1])'''

#Palindrome check

'''text = input("Enter text :").lower()
if text==(text[::-1]):
    print ("Pa")
else:
    print ("Np")'''

#Extract Domain from email

text = input("Enter email :").split("@")

print(text[1])

