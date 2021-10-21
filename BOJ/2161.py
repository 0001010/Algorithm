num = int(input())

x = list(range(1,num+1))
y = list()

for i in range(len(x)-1):
    y.append(x[0])
    x.remove(x[0])
    x.append(x[0])
    x.remove(x[0])
    
result = y+x
print(' '.join(str(e) for e in result))

    


