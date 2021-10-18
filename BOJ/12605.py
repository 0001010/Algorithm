input_num = int(input())
inputs = []

for i in range(input_num):
    x = input().split()
    inputs.append(x)

num = 0
for w in inputs:
    w.reverse()
    num+=1
    print('Case #'+str(num)+': '+' '.join(w))
    
