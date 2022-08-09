# 18870
# 맞을까 싶긴한데 일단 두 예제 모두 OK'
# 딕셔너리로 풀자

n = int(input())
lists = list(map(int, input().split()))

uq = sorted(list(set(lists)))
dic = {uq[i]: i for i in range(len(uq))}

for i in lists:
    print(dic[i], end = ' ')