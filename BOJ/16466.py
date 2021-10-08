import sys

ticket_num = int(input())
first_sold = list(map(int, sys.stdin.readline().split()))
first_sold.sort()

chance = 1
for i in first_sold:
    if i==chance:
        chance+=1
    else:
        print(chance)
        sys.exit(0)
    
print(first_sold[-1]+1)
