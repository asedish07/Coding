def solution(s):
    answer = True
    list_a = []
    # [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
    for i in s:
        if i == '(':
            list_a.append(i)
        else:
            if len(list_a) == 0:
                return False
            else:
                list_a.pop(-1)
    if len(list_a) == 0:
        return True
    else:
        return False