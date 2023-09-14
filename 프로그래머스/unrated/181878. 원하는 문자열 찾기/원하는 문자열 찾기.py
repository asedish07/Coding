def solution(myString, pat):
    if pat.lower() in myString.lower():
        answer = 1
    else:
        answer = 0
    return answer