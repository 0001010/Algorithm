"""
자료구조에서 스택부분이네
nums에 input한 숫자들을 다 넣음
max_height를 nums의 가장 하단이라고 지정
for문이 input_num만큼 돌아감
돌아가면서 nums에서 하나씩 빼서 max_height와 비교함
max_height보다 크면 ok에 1을 더함
그리고 max_height를 그 숫자로 갱신함

모두 다 돌아가면 ok를 출력
"""

import sys
input = sys.stdin.readline

input_num = int(input())
nums = []


for i in range(input_num):
    num = int(input())
    nums.append(num)

max_height = nums[-1]
ok = 1

for w in range(input_num):
    temp = nums.pop()
    if max_height < temp:
        ok+=1
        max_height = temp

print(ok)
