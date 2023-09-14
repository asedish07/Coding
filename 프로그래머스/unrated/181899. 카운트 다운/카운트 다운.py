def solution(start, end_num):
    answer = []
    while True:
        if start < end_num:
            break
        answer.append(start)
        start -= 1
    return answer