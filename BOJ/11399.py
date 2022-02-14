# 11399
num = int(input())
lists = list(map(int, input().split()))

lists.sort()
sums = lists[0]
lists_ans = [lists[0]]

for i in range(1, len(lists)):
    sums+=lists[i]
    lists_ans.append(sums)
    
print(sum(lists_ans))