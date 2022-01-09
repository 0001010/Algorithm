# 1676

def p(n):
    y = 1
    for i in range(n,0,-1):
        y*=i
        
    return y

def sol():
    n = int(input())
    y = p(n)
    y = list(map(str, str(y)))[::-1]

    zero_count = 0

    for i in y:
        if i!='0':
            break
        else:
            zero_count+=1
            
    return zero_count

solution = sol()
print(solution)
