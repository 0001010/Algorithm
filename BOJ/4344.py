input_num = int(input())

over_rat = []
for put in range(input_num):
    mean = 0
    person_num = 0
    class_score = list(map(int, input().split()))
    mean+= ((sum(class_score)-class_score[0])/(len(class_score)-1))
    
    for i in class_score[1:]:
        if mean< i:
            person_num+=1
        else:
            pass

    over_ratio = round(person_num/(len(class_score)-1)+0.00000001,6)
    over_rat.append(over_ratio)

for w in over_rat:
    print('{:.3%}'.format(w))