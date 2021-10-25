first = input()
second = input()

first_word = []
second_word = []

max_length = len(first)*len(second)

for i in range(int(max_length/(len(first)))):
    first_word.append(first)

for w in range(int(max_length/(len(second)))):
    second_word.append(second)
    
if ''.join(first_word)==''.join(second_word):
    print(1)
else:
    print(0)
