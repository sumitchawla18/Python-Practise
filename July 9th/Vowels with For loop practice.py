''' consonants
vowel = ['a', 'e', 'i', 'o', 'u']
word = input("Enter the string :")
c = 0
for i in word:
    if i not in vowel:
        c+=1
print(c)'''

'''#program for Vowels
vowel = ['a', 'e', 'i', 'o', 'u']
word = input("Enter the string :")
c = 0
for i in word:
    if i in vowel:
        c+=1
print(c)'''

'''#program for vowels and consto        
vowel = ['a', 'e', 'i', 'o', 'u']
word = input("Enter the string :")
c = 0
d = 0

for i in word:
    if i in vowel:
        c+=1 
    elif i not in vowel:
        d+=1
        
print (f"Vowels in the string are {c}")
print(f"Conso in the string are {d}")'''

'''#Program to count number of alphabets in the word

word = input("Enter any word :").lower()
use = input("Enter any alphabet:").lower()
c = 0

for i in word:
    if i in use:
        c+=1
print(f"Number of times, {use} appears in {word} is {c}")'''


'''#Finding the maximum number in a list

numList =[5,85,35,89,125,120,20,188,158,168,2,5]
c = 0
d = 0
for i in range(len(numList)-1):
    if numList[i] > c:
        c = numList[i]
        d = i
print(c)'''

#Finding the maximum number in a list without using range

numList =[500,85,35,89,125,120,20,1808,158,168,2,5]
c = 0
for i in numList:
    if i > c:
        c=i
print(c)
                 


