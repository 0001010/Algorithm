"""
단순 수학문제이다.

어떤 수던지 1*1*...로 표현 가능 
그래서 모든 수에 대해서 yes
"""
case = int(input())

for i in range(case):
    inputs = list(map(int, input().split()))
    print('yes')