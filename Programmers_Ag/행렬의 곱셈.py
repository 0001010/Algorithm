def solution(arr1, arr2):
    answer = [[0 for i in range(len(arr2[0]))] for j in range(len(arr1))]

    for i in range(len(arr1)):
        for j in range(len(arr2[0])):
            for z in range(len(arr1[0])):
                answer[i][j]+=(arr1[i][z]* arr2[z][j])
    return answer