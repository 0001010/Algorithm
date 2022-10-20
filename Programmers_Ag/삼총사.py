from itertools import combinations

def solution(number):
    answer = 0
    number = map(str, number)
    com = combinations(number, 3)
    for i in com:
        if sum(map(int,i))==0:
            answer+=1
    
    return answer