# 2670
# dp 문제이다.
# lists를 만들어 현재자리와 바로 이전자리*현재자리 해서 둘 중 max값을 찾아내서 현재자리에 삽입

num = int(input())

lists = []

for i in range(num):
    lists.append(float(input()))
    
for j in range(1, num):
    lists[j] = max(lists[j], lists[j-1]*lists[j])

print('{:.3f}'.format(max(lists)))