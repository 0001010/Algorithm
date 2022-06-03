# 10989
# 딕셔너리로 중복되는 것들을 카운트해서 그것들을 출력함
# 처음에 딕셔너리에 key, value값이 없으면 애러가 난다. 이것을 예외처리로 key, value값을 만들어준다

num = int(input())

dic = dict()

for i in range(num):
    x = int(input())
    try:
        dic[x]+=1
    except:
        dic[x] = 1

dic = sorted(dic.items(), key = lambda item:item[0])
for i in dic:
    for j in range(i[1]):
        print(i[0])