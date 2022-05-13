# 9095
# dp문제인것같다.
# 1-> 1, 2-> 2, 3-> 4, 4-> 7 이런식으로 d = d[-1]+d[-2]+d[-3] 표현가능
# 따라서 점화식을 세워주면 끝남

num = int(input())

lists = []
ele = [1,2,4]
for i in range(num):
    lists.append(int(input()))

for j in range(2, max(lists)-1):
    ele.append(ele[j] + ele[j-1] + ele[j-2])

for z in lists:
    print(ele[z-1])