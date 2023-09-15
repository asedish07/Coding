def solution(my_string, is_suffix):
    n = len(my_string) - len(is_suffix)
    if my_string[n:] == is_suffix:
        answer = 1
    else:
        answer = 0
    return answer