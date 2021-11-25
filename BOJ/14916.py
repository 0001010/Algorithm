# 거스름돈

x = int(input())

coin = [5,2]
five = 0
two = 0

five += x//coin[0]
x -= coin[0]*(x//coin[0])

while coin!=0:
    if x%coin[1]!=0:
        five-=1
        x+=coin[0]
    else:
        two += x//coin[1]
        x -= coin[1]*(x//coin[1])
        break
if five<0:
    print(-1)
else:
    print(five+two)
# 거스름돈을 줄수 없는경우? -1