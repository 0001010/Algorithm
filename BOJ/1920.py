# 1920
# 이분탐색으로 풀면 되는데 2개의 리스트중 하나를 고정하고 거기에 있는 원소를 탐색하는 식으로 진행하면 된다

one = int(input())
one_input = list(map(int, input().split()))
two = int(input())
two_input = list(map(int, input().split()))

one_input.sort()

def bs(lists, num):
    start = 0
    end = len(lists)-1
    while start <= end:
        mid = (start + end)//2
        if lists[mid]==num:
            return 1
        elif lists[mid]<num:
            start = mid + 1
        else:
            end = mid - 1
    return 0

for i in two_input:
    print(bs(one_input, i))