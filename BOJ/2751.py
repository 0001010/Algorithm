from sys import stdin

input_=int(stdin.readline())
arr=[]
for i in range(input_):
    x=int(stdin.readline())
    arr.append(x)
arr.sort()
for i in range(input_):
    print(arr[i])
