def solution(s):
    answer = [0]*(len(s))
    s = list(s)
    alph = ''
    
    for i in range(len(s)):
        if s[i] not in alph:
            alph+=(s[i])
            answer[i] = -1
        else:
            answer[i] = i-(s.index(s[i]))
            s[s.index(s[i])] = ' '
            alph+=s[i]
            
    
    return answer