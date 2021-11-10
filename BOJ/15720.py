# 15720 카우버거
"""
Main Idea

세트 할인은 3가지가 모두 충족 되었을때 된다.
그러므로 최소 가격 = 최대 할인

최대 할인을 받으려면 지불 값이 최대
즉, b,c,d가 모두 최대가 되고 b,c,d가 세트 할인이 들어가면 된다.

b,c,d를 역순으로 정렬하고 각 리스트의 원소끼리 더해주고 할인해준다.
세트가 아닌 원소들은 그냥 다 더해버리면 된다.
"""
b, c, d = list(map(int, input().split()))

b_price = list(map(int, input().split()))
c_price = list(map(int, input().split()))
d_price = list(map(int, input().split()))

b_price.sort(reverse = True)
c_price.sort(reverse = True)
d_price.sort(reverse = True)


lists_price = [len(b_price),len(c_price),len(d_price)]
lower_price = 0
for i in range(min(lists_price)):
    lower_price += (b_price[i] + c_price[i] + d_price[i])*0.9
    
lower_price += sum(b_price[min(lists_price):])
lower_price += sum(c_price[min(lists_price):])
lower_price += sum(d_price[min(lists_price):])

print(sum(b_price) + sum(c_price) + sum(d_price))
print(int(lower_price))