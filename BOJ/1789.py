sums = int(input())
i = 0

while sums>=0:
    i+=1
    sums-=i
    
if sums<0:
    print(i-1)
else:
    print(i)
