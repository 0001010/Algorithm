def solution(n):
    answer = ''
    while n>0:
        n, mod = divmod(n,3)
        answer += str(mod)
    sums = 0
    count = 0
    for i in answer[::-1]:
        sums+=int(i)*(3**count)
        count+=1
    return sums