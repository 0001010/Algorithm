def solution(s):
    s = s.split(" ")
    answer = []
    for i in s:
        ss = ''
        for j in range(len(i)):
            if j%2==0:
                ss+=i[j].upper()
            elif j%2==1:
                ss+=i[j].lower()
        answer.append(ss)
    answer = " ".join(answer)
    return answer