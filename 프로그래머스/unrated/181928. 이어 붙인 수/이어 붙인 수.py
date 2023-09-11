def solution(num_list):
    even_n = 0
    odd_n = 0
    for i in range(len(num_list)):
        if num_list[i] % 2 == 0:
            even_n += 1
        else:
            odd_n += 1
    even_cnt = 10 ** even_n /10
    odd_cnt = 10 ** odd_n /10
    even = 0
    odd = 0
    for i in range(len(num_list)):
        if num_list[i] % 2 == 0:
            even += num_list[i] * even_cnt
            even_cnt /= 10
        else:
            odd += num_list[i] * odd_cnt
            odd_cnt /= 10
    answer = odd + even
    return answer