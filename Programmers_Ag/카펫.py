def solution(brown, yellow):
    answer = []
    for i in range(yellow, 0, -1):
        if yellow%i==0:
            x = i
            y = yellow//i
            if x==1 or y==1:
                pass
            else:
                if x<=y:
                    break
            ans = (x+2)*2 + (y*2)
            if ans==brown:
                break
            if x<y:
                x, y = y, x
    return x+2, y+2