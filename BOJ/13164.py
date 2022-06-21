# 13164
# 최소비용을 구하는 문제로 아이들을 그룹화해서 그 차이가 최소가 되면 된다.
# 인접한 두 원소 사이의 차이를 모두 계산후 정렬해서 차례대로 n-k까지 값을 더해나가면 최소비용을 구할 수 있다.


n, k = list(map(int, input().split()))
inputs = list(map(int, input().split()))
sol = []

for i in range(1, n):
    sol.append(inputs[i]-inputs[i-1])
    
sol.sort()
ans = 0

for j in range(n-k):
    ans+=sol[j]

print(ans)