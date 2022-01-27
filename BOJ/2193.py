# 2193
# num이 1일때 2일때 3일때 해보면 피보나치 인 것을 확인 할 수 있음

num = int(input())

lists = [1,1]

for i in range(1, num-1):
    lists.append(lists[i]+lists[i-1])
print(lists[-1])
