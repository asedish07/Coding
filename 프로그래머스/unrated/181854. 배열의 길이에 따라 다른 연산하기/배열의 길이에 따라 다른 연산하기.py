def solution(arr, n):
    answer = []
    if len(arr) % 2 == 0:
        for i in range(len(arr)):
            if i % 2 == 0:
                answer.append(arr[i])
            else:
                answer.append(arr[i] + n)
    else:
        for i in range(len(arr)):
            if i % 2 == 0:
                answer.append(arr[i] + n)
            else:
                answer.append(arr[i])
    return answer