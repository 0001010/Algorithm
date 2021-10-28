"""
python에 set이라는 집합을 표현할수있는 함수가 있으므로 적극 활용하는 것도 좋은 방법일 듯 하다
차집합은 - 혹은 difference로 가능하다
"""
from sys import stdin

input_num = list(map(int, stdin.readline().split()))
a = list(map(int, stdin.readline().split()))
b = list(map(int, stdin.readline().split()))

a = set(a)
b = set(b)
print(len(a-b) + len(b-a))