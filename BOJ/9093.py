n = int(input())

for i in range(n):
    s = ""
    x = input().split()
    for j in x:
        s = s + j[::-1]
        s = s + " "
        
    print(s[:-1])