# 13301 타일 장식물

num = int(input())

lists = [1, 1]
for i in range(2, num):
    lists.append(lists[i-2]+lists[i-1])
if num==1:
    print(lists[0]*4)
else:
    print((lists[-1]+lists[-2])*2 + lists[-1]*2)