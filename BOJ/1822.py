num = list(map(int, input().split()))

a = list(map(int, input().split()))
b = list(map(int, input().split()))

minus = set(a)-set(b)
minus_new = sorted(list(minus))

if len(minus_new)==0:
    print(len(minus_new))
    
else:
    print(len(minus_new))
    print(' '.join(map(str, minus_new)))
