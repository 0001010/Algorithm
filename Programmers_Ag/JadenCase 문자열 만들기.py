def solution(s):
    one = list(s)
    two = s.lower()
    three = list(two)
    
    three[0] = three[0].upper()
    for i in range(len(s)-1):
        if one[i]==' ':
            three[i+1] = one[i+1].upper()

    
    return ''.join(three)