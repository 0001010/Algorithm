# 1158 요세푸스

x,y = list(map(int, input().split()))
x_list = list(range(1, x+1))

removes = []
pop_num = 0

while len(x_list) >0:
    pop_num = (pop_num+(y-1)) % len(x_list)
    pop_ele = x_list.pop(pop_num)
    removes.append(str(pop_ele))
print("<", ", ".join(removes), ">", sep='')
