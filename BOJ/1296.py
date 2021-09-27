minsik = input()
num = int(input())

grils_name = []
grils_proba = []

for i in range(num):
    girl = input()
    grils_name.append(girl)
    minsik_girl = minsik+girl
    L = 0
    O = 0
    V = 0
    E = 0
    for splits in minsik_girl:
        if splits=='L':
            L+=1
        elif splits=='O':
            O+=1
        elif splits=='V':
            V+=1
        elif splits=='E':
            E+=1
        else:
            pass
    proba = ((L+O)*(L+V)*(L+E)*(O+V)*(O+E)*(V+E))%100
    grils_proba.append(proba)
dics = dict(zip(grils_name, grils_proba))
duplicate = [k for k,v in dics.items() if max(dics.values()) == v]
duplicate.sort()
print(duplicate[0])