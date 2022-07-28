s, k = list(map(int, input().split()))

lists = [0]*(k+1)
idx = 0

for i in range(s):
    idx+=1
    if idx<k:
        lists[idx]+=1
    elif idx==k:
        lists[idx]+=1
        idx=0

def prod(lists):
    len_lists = len(lists)
    prod_sum = 1
    for i in range(1, len_lists):
        prod_sum *= lists[i]
    
    return prod_sum

print(prod(lists))

# 리스트를 k개 만큼 만들고 거기에서 for문 돌려가면서 하나씩 추가
# [0, 0, 0] -> [1, 0, 0] -> [1, 1, 0] 이렇게
# 마지막까지 이렇게 되면 최대값을 얻을 수 있음