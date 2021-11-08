num = int(input())
word = dict()

for i in range(num):
    x = input()
    word[x] = len(x)
    
word = sorted(word.items(), key = lambda item : (item[1], item[0])) # 정렬 두번하

for j in word:
    print(j[0])