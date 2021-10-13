counts = int(input())
a = [1]
b = [0]

for i in range(counts):
    a.append(b[i])
    b.append(a[i] + b[i])
print(a[i+1], b[i+1])