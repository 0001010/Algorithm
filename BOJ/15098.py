"""
유니크한 값들만 추려내서
처음입력받은 단어의 갯수와 비교
같으면 yes
다르면 no 출력

"""

word = input().split()

filters = []
for i in word:
    if i not in filters:
        filters.append(i)

if len(word)==len(filters):
    print('yes')
else:
    print('no')
