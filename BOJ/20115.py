num = int(input())
lists = list(map(int, input().split()))
sums = 0
lists.sort()
for i in range(num-1):
    sums+=lists[i]/2
print('%g'%(sums+lists[-1])) # 예시에서는 소수점이 없음
# '%g'%로 소수점을 없애주자