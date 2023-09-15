def solution(arr, n):
    answer = []
    is_odd_length = len(arr) % 2 == 1
    
    for i in range(len(arr)):
        if is_odd_length and i % 2 == 0:
            answer.append(arr[i] + n)
        elif not is_odd_length and i % 2 != 0:
            answer.append(arr[i] + n)
        else:
            answer.append(arr[i])
            
    return answer
