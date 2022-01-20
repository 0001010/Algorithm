# 1541
# eval로 풀려고 하면 0001 이런 것들이 있어서 쉽지않고
# input으로 받은것을 -로 나눈다음 변수 하나를 만들어 나눠진것들을 +로 다시 나눠서 더함
# 나눠지것 오른쪽으로 -가 붙어야 차이가 나서 오른쪽으로 나뉜것들에서 다시 +로 나누고 그것들을 하나씩 빼줌

x = input().split('-')
sums = 0

for i in x[0].split('+'):
    sums += int(i)

for j in x[1:]:
    for s in j.split('+'):
        sums -= int(s)

print(sums)