n=10

num = 0
num1 = 1

for i in range(n):
    calc = num + num1
    num=num1
    num1=calc
    print(calc)
