subj_num = int(input())

grd = {'A+':4.3,'A0':4.0,'A-':3.7,
       'B+':3.3,'B0':3.0,'B-':2.7,
       'C+':2.3,'C0':2.0,'C-':1.7,
       'D+':1.3,'D0':1.0,'D-':0.7, 'F':0.0}

total = 0
grd_num = 0

for subj in range(subj_num):
    subject = input().split()
    grd_num+= int(list(subject)[1])
    total+= int(list(subject)[1])*grd[list(subject)[2]]

avg = round(total/grd_num+0.000000001,2)
print('{:.2f}'.format(avg))
