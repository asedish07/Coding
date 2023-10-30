def solution(array):
    count_list = [0] * 1000
    for i in array:
        count_list[i] += 1
    if sorted(count_list)[-1] == sorted(count_list)[-2]:
        return -1
    else:
        return count_list.index(max(count_list))