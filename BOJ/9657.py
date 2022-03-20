# 9657
# 상근이를 기준으로 1개가 남으면 무조건 상근이가 이기고 2개 남으면 상근이가 무조건 지고 3,4,5개 남으면
# 상근이가 무조건 이기게 된다.
# dp로 상근이 턴일때 i-1번째 즉, i-1번째때 창영이가 가져갔으면 상근이의 승리, 똑같이 i-3,4,5라고 하면 그게 0이면 상근이 승리

num = int(input())
arr = [0]*1001
arr[1] = 1
arr[2] = 0
arr[3] = 1
arr[4] = 1
arr[5] = 1

for i in range(6, len(arr)):
    arr[i] = 0
    if arr[i-1] == 0:
        arr[i] = 1
    if arr[i-3] == 0:
        arr[i] = 1
    if arr[i-4] == 0:
        arr[i] = 1
        
if arr[num]==1:
    print('SK')
else:
    print('CY')