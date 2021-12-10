# 10828

from sys import stdin

n = int(stdin.readline())
stack = []
ans = []

def push(inputs):
    stack.append(inputs)
    
def pop():
    if len(stack)==0:
        ans.append('-1')
    else:
         ans.append(str(stack.pop()))
        
def size():
     ans.append(str(len(stack)))

def empty():
    if len(stack)==0:
         ans.append('1')
    else:
         ans.append('0')
def top():
    if len(stack)==0:
         ans.append('-1')
    else:
         ans.append(str(stack[-1]))


for i in range(n):
    x = stdin.readline().split()
    
    if x[0] == 'push':
        push(x[1])
    elif x[0] == 'pop':
        pop()
    elif x[0] == 'size':
        size()
    elif x[0] == 'empty':
        empty()
    elif x[0] == 'top':
        top()
print('\n'.join(ans))