def solution(s):
    answer = []
    zero = 0
    remain = 0
    count = 0
    while True:
        if s=="1":
            break
        for i in s:
            if i=='0':
                zero+=1
            else:
                remain+=1
        s = format(remain, 'b')
        remain = 0
        count+=1

    return [count, zero]