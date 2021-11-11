
"""
오른쪽으로 밖에 이동을 못하고 자기보다 높은 봉우리가 있으면 뒤에 있는 것들은 닿지 않는다.
그래서 본인보다 큰 숫자가 나오면 break를 걸어줘야함


"""



dragon = int(input())
lists = []

x = list(map(int, input().split()))

for i in range(dragon-1):
    counts = 0
    for w in range(i+1, dragon):
        if x[i]>x[w]:
            counts+=1
        else:
            break
    lists.append(counts)
        
        
print(max(lists))
            

    