def solution(participant, completion):
    
    di = {}
    
    for p in participant:
        if p in di:
            di[p] += 1
        else:
            di[p] = 1
    for c in completion:
        di[c] -= 1

    nzk = [key for key, value in di.items() if value != 0]
    answer = nzk[0]
    
    return answer