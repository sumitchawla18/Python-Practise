# Program to write counter and calculate 6th decimal value of positive,negative and zero

positivecnt = 0
negativecnt = 0
zerocnt = 0
arr = [1,5,-9,-8,-7,0,6,0]
typ = len(arr)
for i in arr:
        if i>0:
            positivecnt+=1
        elif i<0:
            negativecnt+=1
        elif i==0:
            zerocnt+=1
      
print(f"{(positivecnt/typ):.6f}") 
print(f"{(negativecnt/typ):.6f}")
print(f"{(zerocnt/typ):.6f}")
