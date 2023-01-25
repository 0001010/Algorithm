# 4796
# 그리드인데... 반례가 있다.
# 만약 캠핑장 이용일수보다 남은 일수가 많다면 그냥 캠핑장 이용일수로 대체
# 반례를 잘 찾자


num = 0

while True:
    l, p, v = list(map(int, input().split()))
    if l==0 and p==0 and v==0:
        break
    else:
        num+=1
        m = v//p
        s = v%p
        if l<s:
            s = l
        print("Case " + str(num)+":", l*m+s)