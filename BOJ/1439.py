#1439 뒤집기

x = input()
one = x.split('0')
zero = x.split('1')
one = list(filter(None, one)) # 필터로 리스트안에 있는 ''를 없애버림
zero = list(filter(None, zero))
print(min(len(one), len(zero)))