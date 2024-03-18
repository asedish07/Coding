def solution(arr, queries):
    for i in queries:
        tmp = arr[i[0]]
        arr[i[0]] = arr[i[1]]
        arr[i[1]] = tmp
    return arr