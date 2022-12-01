from collections import deque

def solution(N, stages):
    stages = deque(stages)
    dn = len(stages)
    ans = []
    for i in range(1, N+2):
        count = 0
        for j in stages:
            if j==i:
                count+=1
        try:
            ans.append([i,count/dn])
        except:
            ans.append([i,0])
        dn-=count
        
        ans = sorted(ans, key = lambda item:item[1], reverse = True)
        anss = []
        for i in ans:
            if int(i[0])<=N and int(i[0])>0:
                anss.append(i[0])
                
    return anss