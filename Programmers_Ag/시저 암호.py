alph = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p',
        'q','r','s','t','u','v','w','x','y','z']*2
def solution(s, n):
    answer = ''
    for i in s:
        if i.isalpha()==True:
            if i.isupper()==True:
                answer+=alph[(alph.index(i.lower())+n)].upper()
            else:
                answer+=alph[(alph.index(i.lower())+n)]
        else:
            answer+=' '

        
    return answer