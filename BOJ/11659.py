# 11659
# 누적합이라는데 dp를 누적합으로 변경해서 먼저 계산하고 먼저 들어가는 리스트 - 나중에 들어가는 리스트
# 이렇게 해주면 속도가 빠르다


n, m = list(map(int, input().split()))
ranges = list(map(int, input().split()))

sum_ranges = [0]
total = 0

for i in range(len(ranges)):
    total += ranges[i]
    sum_ranges.append(total)

for j in range(m):
    one, two = list(map(int, input().split()))
    print(sum_ranges[two] - sum_ranges[one-1])