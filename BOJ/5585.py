x = int(input())
minus = 1000 - x

paper = [500, 100, 50, 10, 5, 1]

counts = 0

for i in paper:
    if minus>0:
        a = int(minus/i)
        minus -= a*i
        counts +=a
    else:
        pass
    
print(counts)