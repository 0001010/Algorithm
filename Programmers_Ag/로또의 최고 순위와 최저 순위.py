def solution(lottos, win_nums):
    win_nums.sort(reverse = True)
    lottos.sort(reverse = True)
    upper=0
    lower=0
    for i in win_nums:
        if i in lottos:
            upper+=1
            lower+=1
    for j in lottos:
        if j==0:
            upper+=1
    answer = [0,6,5,4,3,2,1]
    if lower==0:
        lower+=1
    if upper==0:
        upper+=1
    return answer.index(upper), answer.index(lower)