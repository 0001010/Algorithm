def solution(food):
    answer = ''
    for i in range(len(food)):
        if i==0:
            pass
        else:
            aa = str(i)*(food[i]//2)
            if len(aa)!=0:
                answer+=aa
    return answer+'0'+answer[::-1]