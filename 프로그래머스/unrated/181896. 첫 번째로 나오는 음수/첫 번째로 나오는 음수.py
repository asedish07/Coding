def solution(num_list):
    minus_index = -1
    for i in range(len(num_list)):
        if num_list[i] < 0:
            minus_index = i
            break
    return minus_index