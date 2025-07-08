no =int(input("Enter the no: "))
fab =[0,1]
for i in range(1,no):
    newfab_1=fab[i]+fab[i-1]
    fab.append(newfab_1)
print(fab)
