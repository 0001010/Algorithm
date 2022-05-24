s = list(input())
lists = []
for j in range(len(s)):
    
    for i in range(len(s)):
        if len(s[j:i+1])>0:
            lists.append(''.join(s[j:i+1]))
            
print(len(set(lists)))