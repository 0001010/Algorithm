# i가 증가할수록 문자열도 범위가 늘어나고 뒤집어서 같으면 바로 breakㄴ

s = input()

for i in range(len(s)):
    if s[i:]==s[i:][::-1]:
        print(len(s)+i)
        break