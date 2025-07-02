'''n=121
flag=""
for i in range(2,n):
    if n%i==0:
        flag="Not Prime"
        break

if flag=="Not Prime":
    print("Not prime")
else:
    print("Prime")'''

# Optimized code
import math

n=109
flag=""
for i in range(2,int(math.sqrt(n))+1):
    if n%i==0:
        flag="Not Prime"
        break

if flag=="Not Prime":
    print("Not prime")
else:
    print("Prime")

