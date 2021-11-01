w = [1]
score = []

while w[-1] != '#':
    word = input()
    w.append(word)
    a = []
    for i in word:
        lower_word = list(i.lower())
        if lower_word[0].isalpha()==True:
            a.extend(lower_word)
            a = list(set(a))
    score.append(str(len(a)))

print('\n'.join(score[:-1]))
