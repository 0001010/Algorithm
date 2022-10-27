# 2776
# 이분탐색문제이다.
# 기준이 되는 리스트를 하나 잡고 for문으로 돌려가면서 있으면 1 없으면 0을 출력

def bs(lists, num):
    start = 0
    end = len(lists)-1
    while start<=end:
        mid = (start + end)//2
        if lists[mid]==num:
            return 1
        elif lists[mid]< num:
            start = mid+1
        else:
            end = mid-1
    return 0
        

t = int(input())
for i in range(t):
    n = int(input())
    one = list(map(int, input().split()))
    m = int(input())
    two = list(map(int, input().split()))
    one.sort()
    for j in two:
        if bs(one, j)>0:
            print(1)
        else:
            print(0)