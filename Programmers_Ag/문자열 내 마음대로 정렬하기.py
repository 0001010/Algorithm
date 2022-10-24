def solution(strings, n):
    ans = sorted(strings, key = lambda x:(x[n], x))
    
    return ans
