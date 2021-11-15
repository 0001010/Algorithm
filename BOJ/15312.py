from string import ascii_uppercase

he = input()
she = input()
alph = {}

o = [3, 2, 1, 2, 3, 3, 2, 3, 3, 2, 2, 1, 2, 2, 1, 2, 2, 2, 1, 2, 1, 1, 1, 2, 2, 1]
for i in range(len(ascii_uppercase)):
    alph[ascii_uppercase[i]] = o[i]

lists = []

for w in range(len(he)):
    lists.append(alph[he[w]])
    lists.append(alph[she[w]])

while len(lists)>2:
    for_list = []
    for e in range(len(lists)-1):
        sums = lists[e]+lists[e+1]
        if sums>=10:
            for_list.append(sums%10)
        else:
            for_list.append(sums)
    lists = for_list
lists = map(str, lists)
print(''.join(lists))
        
# 리스트에 넣어두고 2개 남을때까지 돌려야
