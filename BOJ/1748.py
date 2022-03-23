# 1748
# 여러번 해보니 규칙이 있다.예를 들어 284가 주어지면 100~284까지는 3자리 즉, 185개는 3자리고 10~99까지는 두자리, 1~9까지는 1자리이다.
# 이걸 토대로 수학적으로 계산해서 넘기면 된다.

n = input()
n_str = len(n)
if n_str==1:
    print(int(n))
else:
    b = 0
    for i in range(n_str):
        if n_str==i+1:
            a = (int(n)-(10**(n_str-1)-1))*n_str
        else:
            b += (i+1)*(9*(10**i))
    print(a+b)
        