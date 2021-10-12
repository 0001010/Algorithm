num = int(input())

zero_nums = []

for i in range(num):
    zero_num = 0
    x = list(map(int, input().split()))
    range_num = list(range(x[0], x[1]+1))
    
    for w in range_num:
        a = list(str(w))

        for q in a:
            if q=='0':

                zero_num+=1
                
    zero_nums.append(str(zero_num))

print('\n'.join(zero_nums))


