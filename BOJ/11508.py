# 11508
# 그리디 문제이다. 무조건 3개를 고르면 가장 낮은 가격을 무료로 준다고 하니 list를 뒤집고 인덱스가 3번째이면 pass그렇지 않으면 합산하면 된다


num = int(input())
lists = []
sums = 0
for i in range(num):
    lists.append(int(input()))

lists.sort(reverse = True)

for j in range(num):
    if j%3==2:
        pass
    else:
        sums+=lists[j]

print(sums)