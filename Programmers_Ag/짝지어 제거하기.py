from collections import deque

def solution(s):
    qu = deque()
    for i in s:
        if len(qu)==0:
            qu.append(i)
        else:
            if qu[-1]==i:
                qu.pop()
            else:
                qu.append(i)
    if len(list(qu))==0:
        ans = 1
    else:
        ans = 0

    return ans