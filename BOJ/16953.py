# 16953
a, b = list(map(int, input().split()))
count = 0
while True:
    if b==a:
        break
    if str(b)[-1]=='1':
        b = int(str(b)[:-1])
    else:
        if b%2==0:
            b = int(b/2)
        else:
            count = -1
            break
    if b<a:
        count = -1
        break
    count +=1
    
if count==-1:
    print(count)
else:
    print(count+1)