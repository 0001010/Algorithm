def solution(a, b, n):
    cnt = 0
    while True:
        if n<a:
            break
        change = n//a
        rem = n-(change*a)
        n = rem + change*b
        cnt+=change*b
        print(cnt)

    return cnt