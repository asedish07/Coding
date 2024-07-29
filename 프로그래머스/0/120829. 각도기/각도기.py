def solution(angle):
    answer = 4
    if angle < 90:
        answer = 1
    elif 90 == angle:
        answer = 2
    elif angle < 180:
        answer = 3
    return answer