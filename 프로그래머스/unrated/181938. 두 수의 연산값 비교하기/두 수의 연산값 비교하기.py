def solution(a, b):
    answer = 0
    xplus = ''
    xplus += str(a)
    xplus += str(b)
    answer = a * b * 2
    if int(xplus) > answer:
        return int(xplus)
    else:
        return answer