# 10819
# 순열문제는 permutations로 풀자
# 모든 순열을 저장해두고 for문으로 불로와서 원소하나하나의 차이의 절대값을 계산후 sums에 추가해준다. 
# 그리고 하나의 순열이 끝날때마다 최대값을 갱신해준다.

from itertools import permutations

num = int(input())
lists = list(map(int, input().split()))
per = list(permutations(lists))

ans = 0

for i in per:
    sums = 0
    for j in range(num-1):
        sums+=abs(i[j]-i[j+1])
    ans = max(ans, sums)

print(ans)