def solution(num_list):
    square = 0
    multiply = 1
    for i in range(len(num_list)):
        multiply *= num_list[i]
    for j in range(len(num_list)):
        square += num_list[j]
    if multiply < (square ** 2):
        answer = 1
    else:
        answer = 0
    return answer