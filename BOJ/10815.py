# 10815
# 이분탐색문제인데 이분탐색을 학습히가 좋다.

one = int(input())
list_one = list(map(int, input().split()))
two = int(input())
list_two = list(map(int, input().split()))

list_one.sort()


def bs(lists, num):
    start = 0 # 기본 start변수 0 지정
    end = len(lists)-1 # 기본 end 변수 0 지정
    while start<=end: # start가 end보다 커지면 stop
        mid = (start + end)//2 # 중간인덱스를 찾아서
        if lists[mid]==num: # lists에 중간인덱스가 우리가 찾는 수라면 그대로 mid리턴
            return mid
        elif lists[mid]<num: # 그게 아니고 우리가 찾는수보다 작으면
            start = mid+1 # start에서 mid+1해서 범위를 좁힘
        else: # 우리가 찾는 수보다 크면 end부분에서 mid-1를 해줌
            end = mid-1
    return -1 # 없으면 0

for i in list_two:
    if bs(list_one, i)==-1:
        print(0, end = ' ')
    else:
        print(1, end = ' ')