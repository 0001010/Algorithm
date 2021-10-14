"""
기본 아이디어
최대의 5의 배수를 구한 다음 
나머지를 구한다. 나머지가 3의 배수이면 three_score의 가산
나머지가 3의 배수가 아니면 five_score에서 1을 빼고 다시 if문으로 넘김(이 효과로 five_score와 three_score가 0,0 일 때 -1 출력 가능해짐)

while문을 활용해서 five_score가 0보다 작을때까지 진행

21을 예로 들었을때
21 = 5*4 나머지가 1
나머지가 3의 배수가 아니므로 five_score에서 1을 빼서
21 = 5*3으로 연산 나머지는 6이 남음 6은 3의 배수이므로 몫을 계산해서 three_score에 삽입

즉, 21일때는 5*3 + 3*2로 
3+2 = 5 총 5개가 나옴
"""

kg = int(input())
kgs = [5,3]

five_score = int(kg/kgs[0]) # 5의 배수
three_score = 0 # 3의 배수

while five_score>=0: # while문으로 five_score가 0이상일경우 계속 반복
    if (kg-kgs[0]*five_score)%kgs[1]==0: # 5*five_score을 3으로 나눴을때 나머지가 0일경우
        three_score += int((kg-kgs[0]*five_score)/kgs[1]) # three_score에 몫을 삽입
        break # 이렇게 되면 전부 구하게 되므로 break

    else:
        five_score-=1 # 만약 이게 아니면 five_score에서 1을뺌, while문으로 다시 if문부터 시작
        
print(five_score + three_score)