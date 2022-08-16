def solution(arr1, arr2):
    answer = []
    for one, two in zip(arr1, arr2):
        r = []
        for num in range(len(one)):
            r.append(one[num]+two[num])
        
        answer.append(r)
    return answer