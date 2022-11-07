from collections import Counter

def solution(n):
    answer = 0
    n_format = format(n, 'b')
    count = Counter(n_format)['1']
    while True:
        n+=1
        s = format(n, 'b')
        c = Counter(s)['1']
        if c==count:
            break
    return n