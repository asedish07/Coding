def solution(arr, flag):
    answer = []
    
    for i in range(len(flag)):
        if flag[i]:
            answer += [arr[i] for x in range(arr[i]*2)]
        else:
            answer = answer[:len(answer) - arr[i]]
    
    return answer