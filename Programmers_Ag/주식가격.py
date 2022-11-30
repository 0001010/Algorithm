from collections import deque

def solution(prices):
    answer = []
    qu = deque(prices)
    while qu:
        count = 0
        x = qu.popleft()
        
        for i in qu:
            count+=1
            if x>i:
                break

        answer.append(count)
    return answer