num = int(input())
asw = []
for i in range(num):
    x = list(map(int, input().split()))
    x = x[1:]
    x.sort()
    asws = []
    for j in range(len(x)-1):
        ans = abs(x[j]-x[j+1])
        asws.append(ans)
    asw.append('Class '+str(i+1))
    asw.append('Max '+str(max(x))+', '+'Min '+str(min(x))+', '+'Largest gap '+str(max(asws)))
    
for k in asw:
    print(k)