# 1850
# 최대공약수를 구하는 문제로 유클리드 호제법으로 푼 다음 그 값에 '1'을 넣는 방식으로 진행
a, b = list(map(int, input().split()))

while b>0:
    a, b = b, a%b
    
print('1'*a)