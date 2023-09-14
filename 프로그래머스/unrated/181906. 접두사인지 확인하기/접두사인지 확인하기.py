def solution(my_string, is_prefix):
    n = len(is_prefix)
    if my_string[:n] == is_prefix:
        answer = 1
    else:
        answer = 0
    return answer