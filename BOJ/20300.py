# 20300
# num을 홀짝으로 나눠서 홀수는 먼저 가장 큰 수를 min_val에 넣어두고 왼쪽 오른쪽 끝에 있는 value값들을 가져와서 더해준다음 최대값이면 갱신
# 짝수면 가장 큰수를 넣지말고 바로 양쪽 끝 수를 비교

num = int(input())
lists = list(map(int, input().split()))
lists.sort()
min_value = 0

if num%2==1:
    min_value = lists.pop()
    lenght = len(lists)//2
    
    for i in range(lenght):
        vi = lists.pop() + lists.pop(0)
        min_value = max(vi, min_value)

else:
    lenght = len(lists)//2
    
    for j in range(lenght):
        vi = lists.pop() + lists.pop(0)
        min_value = max(vi, min_value)

print(min_value)