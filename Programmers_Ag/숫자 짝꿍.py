from collections import Counter

def solution(X, Y):
    X = Counter(X)
    Y = Counter(Y)
    answer = "-1"
    XY = X&Y
    XY = sorted(XY.items(), reverse = True)
    if XY:
        answer = ""
        for x,y in XY:
            answer+=(x*y)
        if sum(list(map(int, answer)))==0:
            answer = "0"

    return answer