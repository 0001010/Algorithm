from itertools import combinations

l, c = list(map(int, input().split()))
lists = list(input().split())
lists.sort()
vo = ['a', 'e', 'i', 'o', 'u']

com = combinations(lists, l)

for i in com:
    vo_count = 0
    cons = 0
    for j in list(i):
        if j in vo:
            vo_count+=1
        else:
            cons+=1
            
    if vo_count>0 and cons>1:
        print(''.join(list(i)))
