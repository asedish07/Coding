def solution(num_list):
    len_list = len(num_list)
    sum = 0
    if len_list >= 11:
        for i in range(len_list):
            sum += num_list[i]
    else:
        sum = 1
        for i in range(len_list):
             sum *= num_list[i]
    return sum