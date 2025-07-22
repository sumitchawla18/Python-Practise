a = [4, 2, 3]
b = [3, 2, 1]
alictr=0
bobctr=0
for i in range(len(a)):
    for j in range(len(b)):
        if i==j:# i == j are the Indexes. We need to ensure that both indexes are equal before accessing the elements
            if a[i]>b[j]:
                alictr+=1
            elif a[i]<b[j]:
                bobctr+=1
            #print(a[i],b[j])

print(alictr)
print(bobctr)
    
