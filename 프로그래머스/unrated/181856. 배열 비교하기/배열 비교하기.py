def solution(arr1, arr2):
    sumf = sum(arr1)
    sums = sum(arr2)
    answer = 0
    if len(arr1) > len(arr2):
        answer = 1
    elif len(arr2) > len(arr1):
        answer = -1
    else:
        if sumf > sums:
            answer = 1
        elif sums > sumf:
            answer = -1
        else:
            answer = 0
    return answer