# 10866

from collections import deque

dq = deque()

def push_front(x):
    dq.appendleft(x)

def push_back(x):
    dq.append(x)

def pop_front():
    if len(dq)==0:
        print(-1)
    else:
        print(dq.popleft())

def pop_back():
    if len(dq)==0:
        print(-1)
    else:
        print(dq.pop())

def size():
    print(len(dq))

def empty():
    if len(dq)==0:
        print(1)
    else:
        print(0)

def front():
    if len(dq)==0:
        print(-1)
    else:
        print(dq[0])
        
def back():
    if len(dq)==0:
        print(-1)
    else:
        print(dq[-1])

num = int(input())
for i in range(num):
    inputs = input().split()
    if inputs[0]=='push_front':
        push_front(int(inputs[1]))
    elif inputs[0]=='push_back':
        push_back(int(inputs[1]))
    elif inputs[0]=='pop_front':
        pop_front()
    elif inputs[0]=='pop_back':
        pop_back()
    elif inputs[0]=='size':
        size()
    elif inputs[0]=='empty':
        empty()
    elif inputs[0]=='front':
        front()
    elif inputs[0]=='back':
        back()