# 9237
num = int(input())
lists = list(map(int, input().split()))
    
lists.sort(reverse= True)
add = 1
max_num = 0
for j in lists:
    if max_num<j+add:
        max_num = j+add
    add+=1
print(max_num+1)