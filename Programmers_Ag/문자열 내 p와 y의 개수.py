def solution(s):
    p = 0
    y = 0
    answer = True
    
    s = s.lower()
    for i in s:
        if i=='p':
            p+=1
        elif i=='y':
            y+=1
    if p!=y:
        answer = False

    return answer