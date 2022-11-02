def solution(n, arr1, arr2):
    arr1_new = []
    arr2_new = []
    graph = [["#"]*n for i in range(n)]
    ans = []
    for i in range(n):
        a = format(arr1[i],'b').zfill(n)
        b = format(arr2[i],'b').zfill(n)
        for j in range(n):
            if a[j]=='0':
                graph[i][j]=' '
            if b[j]=='0' and graph[i][j]==" ":
                graph[i][j]=' '
            else:
                graph[i][j]='#'
        ans.append(''.join(graph[i]))

    
    return ans