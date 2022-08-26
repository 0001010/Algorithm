# 4358
# defaultdict을 만드는것도 좋은 방법이다.
# rstrip은 오른쪽 빈칸을 제거함
# count를 세주고 정렬해서 100분위로 표시 한 후 출력
# 입력갯수가 정해져있지 않으서 입력이 없다면 자동적으로 멈추는 것을 실행


from sys import stdin
from collections import defaultdict, Counter

count = 0
lists = defaultdict(int)

while True:
    x = input().rstrip()
    if x=="":
        break
    lists[x] += 1 # dic에 원소를 넣으면서 count
    count += 1
    
dic = Counter(lists)
for key in dic:
    dic[key] /= count/100

dic = sorted(dic.items(), key = lambda item: item[0])

for z in dic:
    print(z[0], "{:.4f}".format(z[1]))
