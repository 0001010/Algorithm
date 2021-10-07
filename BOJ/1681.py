x = list(map(int, input().split()))

a = 0
an = []

while len(an)<x[0]:
    a+=1
    if str(x[1]) in list(str(a)):
        pass
    else:
        an.append(a)
        
print(an[-1])
