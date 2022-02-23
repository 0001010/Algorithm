# 1009
# 제곱수를 해봐서 반복되는걸 찾는다.

num = int(input())
for i in range(num):
    a, b = list(map(int, input().split()))
    a = a%10
    
    if a == 1 or a == 5 or a == 6:
        print(a)
    elif a == 4 or a == 9:
        b = b%2
        if b==1:
            print(a)
        else:
            print((a**2)%10)
    elif a==0:
        print(10)
    else:
        b = b%4
        if b==0:
            print((a**4)%10%10%10)
        else:
            print((a**b)%10%10%10)