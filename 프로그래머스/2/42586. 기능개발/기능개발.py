import math

def solution(progresses, speeds):
    answer = []
    lst = []
    for i in range(len(progresses)):
         lst.append(math.ceil((100 - progresses[i]) / speeds[i]))
    cnt = 0
    gi = lst[0]
    for i in lst:
        if i <= gi:
            cnt += 1
        else:
            gi = i
            answer.append(cnt)
            cnt = 1
    answer.append(cnt)   
    return answer