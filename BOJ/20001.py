"""
기본 스택문제이다.

스택의 갯수가 0이고 인풋이 고무오리라면 문제를 두개 추가
인풋이 고무오리면 가장 최근것을 뺀다.
그 외에 것은 문제를 추가

마지막에 고무오리 디버깅 끝이 문제로 들어가므로 스택의 갯수를 하나 빼줘서 if문 돌리면 된다.
"""


start = input()
stack = []
while start!='고무오리 디버깅 끝':
    start = input()
    if start == '고무오리' and len(stack) == 0:
        stack.append('문제')
        stack.append('문제')
    elif start == '고무오리':
        stack.pop()
    else:
        stack.append('문제')

if len(stack)-1 == 0:
    print('고무오리야 사랑해')
else:
    print('힝구')
