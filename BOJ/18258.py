# 18258
from collections import deque

q = deque()

def push(x):
    q.append(x)

def pop():
    if len(q)==0:
        print(-1)
    else:
        print(q.popleft())

def size():
    print(len(q))

def empty():
    if len(q)==0:
        print(1)
    else:
        print(0)

def front():
    if len(q)==0:
        print(-1)
    else:
        print(q[0])

def back():
    if len(q)==0:
        print(-1)
    else:
        print(q[-1])
        
n = int(input())
for i in range(n):
    inputs = input().split()
    if inputs[0]=='push':
        push(int(inputs[1]))
    elif inputs[0]=='pop':
        pop()
    elif inputs[0]=='size':
        size()
    elif inputs[0]=='empty':
        empty()
    elif inputs[0]=='front':
        front()
    else:
        back()