'''
1. prices를 돌면서 queue에 넣기.
2. 각각 값을 queue에 넣으면서 주가가 떨어지는 때가 오면 값을 빼
'''


def solution(prices):
    n = len(prices)
    answer = []
    cnt = 0
    for i in range(n - 1):
        cnt = 0
        for j in range(i + 1, n):
            if prices[i] <= prices[j]:
                cnt += 1
            else:
                cnt += 1
                break
        answer.append(cnt)
    answer.append(0)
    return answer