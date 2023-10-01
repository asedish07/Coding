def solution(arr, intervals):
    answer = []
    f = 0
    s = 0
    for i in intervals:
        f = i[0]
        s = i[1]
        for j in range(f, s + 1):
            answer.append(arr[j])
    return answer                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  