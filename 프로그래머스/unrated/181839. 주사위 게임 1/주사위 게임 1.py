def solution(a, b):
    answer = 0
    if a % 2 == 1 and b % 2 == 1:
        answer = a ** 2 + b ** 2
    elif a % 2 == 1 or b % 2 == 1:
        answer = (a + b) * 2
    else:
        answer = abs(a - b)
    return answer