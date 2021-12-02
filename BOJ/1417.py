# 국회의원 선거 1417
"""
own이라는 기호1번 인 사람의 value값이 max가 되는 시점을 찾는다. own은 한개의 값밖에 없음
people은 기호 1번을 제외하고 전부 들어가있다. people의 max값이 own의 값보다 작아지는 시점까지
people의 max로 잡히는 값들을 -1씩 하고 own은 +1씩 한다.

people의 max값이 own보다 작아지면 counts를 출력

"""
person = int(input())

people = []

for i in range(person):
    num = int(input())
    people.append(num)
    
own = people[:1]
people.remove(people[0])
counts = 0

if len(people)==0:
    print(counts)
else:
    while max(people)>=own[0]:
        people[people.index(max(people))]-=1 # max인값의 인덱스를 찾아서 계속 줄여나감
        own[0]+=1
        counts+=1
    print(counts)
    

    # input의 max인 친구들을 계속 줄여나가야함 그래서 본인이 max가 되면 당선임
    # 문제는 리스트에서 max인 친구들이 다수면 안됨 이게 제일 문제네
    # value에러?