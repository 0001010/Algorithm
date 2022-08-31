# 1935
# input으로 받는 'ABCD'문자랑 숫자랑 맵핑을 해야함 많은 사람들이 아스키코드를 이용해서 변환후 인덱스로 사용

num = int(input())
inputs = input()

number = []
for i in range(num):
    x = int(input())
    number.append(x)

stack = []

for i in inputs:
    if 'A' <=i <= 'Z':
        stack.append(number[ord(i) - ord('A')]) # 아스키코드 변환후 인덱스 사용
    else:
        two = stack.pop()
        one = stack.pop()
        
        if i=='+':
            stack.append(one+two)
        elif i=='-':
            stack.append(one-two)
        elif i=='*':
            stack.append(one*two)
        else:
            stack.append(one/two)
print('%.2f'%stack[0])