num = input().split()
reverse_num = 0

for i in num:
    reverse = i[::-1]
    reverse_num+=(int(reverse))
    
print(int(str(reverse_num)[::-1]))
