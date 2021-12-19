num = int(input())

t_num = [0]*36
t_num[0] = 1


for i in range(1, num+1):
    for j in range(0, i):
        t_num[i] += t_num[j]*t_num[i-j-1]

print(t_num[num])