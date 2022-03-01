num = int(input())
dic = list()

for i in range(num):
    inputs = input().split()
    inputs[0] = int(inputs[0])
    dic.append(inputs)
    
dic = sorted(dic, key = lambda item:item[0])
for j in dic:
    print(j[0], j[1])