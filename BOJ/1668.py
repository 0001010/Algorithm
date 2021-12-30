# 1668

num = int(input())
lists = []

for i in range(num):
    x = int(input())
    lists.append(x)

def pros(lists):
    max_height = 0
    count = 0
    for j in range(len(lists)):
        if lists[j]>max_height:
            count+=1
            max_height = lists[j]
    return count

print(pros(lists = lists))
print(pros(lists = lists[::-1]))