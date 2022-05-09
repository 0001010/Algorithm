# 6603
# EOFEroor가 뜨므로 예외처리를 하야한다.
# 기본적인 조합문제이므로 compination을 사용하면 된다.

from itertools import combinations

while True:
    try:
        lists = list(map(str, input().split()))
        if len(lists)==0:
            break
        else:
            com = combinations(lists[1:], 6)
            for i in com:
                print(' '.join(i))
            print('')
    except:
        break

        