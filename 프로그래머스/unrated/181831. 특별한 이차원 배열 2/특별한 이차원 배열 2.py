def solution(arr):
    answer = 0
    cnt = 0
    n = len(arr)
    for i in range(n):
        for j in range(n):
            if arr[i][j] == arr[j][i]:
                cnt += 1
    if cnt == n ** 2:
        answer = 1
    return answer