# 괄호 회전하기

# - 일단 올바른 괄호 검사 함수를 만들기
# - deque를 이용 popleft해서 회전시키기
# - 회전하면서 올바른 괄호검사하기

from collections import deque

def decision(s):
    lists = []
    ans = 0
    for i in s:
        if len(lists)>0:
            if i==']' and lists[-1]=='[':
                lists.pop(-1)
            elif i==')' and lists[-1]=='(':
                lists.pop(-1)
            elif i=='}' and lists[-1]=='{':
                lists.pop(-1)
            else:
                lists.append(i)
        else:
              lists.append(i)
    
    if len(lists)==0:
        ans = 1
    
    return ans
        

def solution(s):
    qu = deque(s)
    answer = 0
    
    for i in range(len(qu)):
        ans = decision(qu)
        string = qu.popleft()
        qu.append(string)
        
        answer+=ans
    
    return answer