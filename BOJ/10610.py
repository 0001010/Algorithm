# 10610
# 최대의 30배수를 만들어야하므로 입력받은 수를 list로 변환후 역정렬
# 후 30배수면 그것을 출력 아니면 -1 출력

num = int(input())
lists = list(map(str, str(num)))

if '0' not in lists:
    print(-1)
else:
    lists.sort(reverse = True)
    if int(''.join(lists))%30==0:
        print(int(''.join(lists)))
    else:
        print(-1)