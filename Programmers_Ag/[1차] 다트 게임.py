def solution(dartResult):
    answer = []
    s = ''
    for i in range(len(dartResult)):
        
        if dartResult[i].isnumeric()==True:
            if dartResult[i-1:i+1]=='10':
                answer.pop()
                answer.append(int(dartResult[i-1:i+1]))
            else:
                answer.append(int(dartResult[i]))
            
        if dartResult[i]=='D':
            answer[-1] = answer[-1]**2
        elif dartResult[i]=='T':
            answer[-1] = answer[-1]**3
        if dartResult[i]=='*':
            if len(answer)==1:
                answer[0] = answer[0]*2
            else:
                answer[-1] = answer[-1]*2
                answer[-2] = answer[-2]*2
        if dartResult[i]=='#':
            answer[-1] = answer[-1]*(-1)
        
    return sum(answer)
