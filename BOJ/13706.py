# 13706

# 인풋으로 들어온 수를 제곱근하는건데 너무 큰 수가 들어오면 overflow가 걸려버린다
# 그래서 이분탐색을 활용하면 풀 수 있다.

num = int(input())

start = 1
end = num
while start<=end:
    mid = (start + end)//2
    if mid**2==num:
        print(mid)
        break
    elif mid**2>num:
        end = mid-1
    else:
        start = mid+1