# 1302번 베스트셀러
"""
sells에 원소를 다 넣어둔다.
그리고 sells의 유니크한 값을 추출해서 변수에 저장
sells의 각 단어의 갯수를 count
딕셔너리로 만듬
딕셔너리에서 value값 정렬을 시도
key = lambda item : item[1] 에서 item[1]은 value값

max_a값을 만들어서 max_a랑 같은 value를 가진 원소들을 다시정렬(알파벳순으로)
"""


x = int(input())
sells = []

for i in range(x):
    inputs = input()
    sells.append(inputs)

unique_sells = list(set(sells))
unique_dic = dict()

for w in unique_sells:
    unique_dic[w] = sells.count(w)
    
a = sorted(unique_dic.items(), key = lambda item :item[1], reverse = True)
max_a = max(unique_dic.values())

lists = []
for e in range(len(a)):
    if max_a==a[e][1]:
        lists.append(a[e][0])
lists.sort()
print(lists[0])