import heapq # 힙 문제 풀때 쓰자
from sys import stdin

input = stdin.readline

num = int(input())

hq = []
for i in range(num):
    inputs = int(input())
    
    if inputs:
        heapq.heappush(hq,(-inputs, inputs)) # 최대힙을 구하는 것
    else:
        if len(hq)>0:
            print(heapq.heappop(hq)[1]) # 튜플로 들어가있어서 원소를 반환하려면 [1]이 필요
        else:
            print(0)