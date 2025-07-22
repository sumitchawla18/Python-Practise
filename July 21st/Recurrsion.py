import sys
sys.set_int_max_str_digits(0)
en = int(input ("Enter the number: "))
fact = 1
for i in range(1,en+1):
    fact=fact*i
print(fact)

'''n = int(input ("Enter the number: "))
def fact(n):
    if n == 0:
        return 1
    else:
        return fact(n-1)*n
print(fact(n))'''
    
        
