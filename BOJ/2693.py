case = int(input())
lists = []
for i in range(case):
    inputs = list(map(int, input().split()))
    inputs.sort(reverse = True)
    lists.append(inputs[2])

for j in lists:
    print(j)
