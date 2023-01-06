def solution(k, m, score):
    score.sort(reverse = True)
    answer = 0
    for i in range(1, (len(score)//m)+1):
        answer+=(min(score[m*(i-1):m*i])*m)
    
    return answer