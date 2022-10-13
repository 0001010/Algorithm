def solution(answers):
    n = len(answers)
    one = [1,2,3,4,5]
    two = [2,1,2,3,2,4,2,5]
    three = [3,3,1,1,2,2,4,4,5,5]
    
    one = [1,2,3,4,5]*(int(n//len(one))+1)
    two = [2,1,2,3,2,4,2,5]*(int(n//len(two))+1)
    three = [3,3,1,1,2,2,4,4,5,5]*(int(n//len(three)+1))
    
    ans_num = [0,0,0]
    
    for i in range(n):
        if one[i]==answers[i]:
            ans_num[0]+=1
        if two[i]==answers[i]:
            ans_num[1]+=1
        if three[i]==answers[i]:
            ans_num[2]+=1
    max_value = max(ans_num)
    ans = []
    
    for i in range(len(ans_num)):
        if ans_num[i]==max_value:
            ans.append(i+1)
    return ans
