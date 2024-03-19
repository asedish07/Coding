def solution(arr, queries):
    answer = []
    for i in queries:
        tmp = []
        for j in range(len(arr)):
            if (j >= i[0]) and (j <= i[1]) and (arr[j] > i[2]):
                tmp.append(arr[j])
        if len(tmp) == 0:
            answer.append(-1)
        else:
            a = min(tmp)
            answer.append(a)
    return answer