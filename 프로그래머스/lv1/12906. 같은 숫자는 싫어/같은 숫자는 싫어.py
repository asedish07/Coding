def solution(arr):
    answer = []
    j = 0
    answer.append(arr[0])
    # [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
    for i in arr:
        if i != answer[j]:
            answer.append(i)
            j += 1
    return answer