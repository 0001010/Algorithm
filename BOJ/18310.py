num = int(input())

n = list(map(int, input().split()))

n.sort()
print(n[int((len(n)+1)/2) -1])