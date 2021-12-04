# 1065 한수


x = int(input())
count = 0
if x<100:
    print(x)
else:
    for num in range(100,x+1):
        str_x = list(str(num))
        j = []
        for i in range(len(str_x)-1):
            a = int(str_x[i])-int(str_x[i+1])
            j.append(a)
        if j[0]==j[1]:
            count+=1
            
    print(count+99)