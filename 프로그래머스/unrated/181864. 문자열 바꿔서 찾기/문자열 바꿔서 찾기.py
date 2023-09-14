def solution(myString, pat):
    myString_n = ''
    pat_n = ''
    for i in myString:
        if i == 'A':
            myString_n += 'B'
        else:
            myString_n += 'A'
    if pat in myString_n:
        answer = 1
    else:
        answer = 0
    return answer