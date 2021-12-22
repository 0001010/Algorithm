num = int(input())

lists = [1,1,1]
nums = []
for i in range(num):
    nums.append(int(input()))

for j in range(max(nums)-3):
    lists.append(lists[j]+lists[j+1])
    
for z in nums:
    print(lists[z-1])