def solution(my_string, overwrite_string, s):
    answer = ''
    for i in range(0, s):
        answer += my_string[i]
    for i in overwrite_string:
        answer += i
    for j in range(len(overwrite_string) + s, len(my_string)):
        answer += my_string[j]
    return answer