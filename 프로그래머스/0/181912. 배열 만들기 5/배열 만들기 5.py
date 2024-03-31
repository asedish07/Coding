def solution(intStrs, k, s, l):
    answer = []
    for i in intStrs:
        a = int(i[s:l+s])
        if a > k:
            answer.append(a)
    return answer