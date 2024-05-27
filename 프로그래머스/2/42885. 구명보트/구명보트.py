'''
return 최소한으로 필요한 구명보트의 개수

1. 사람들의 몸무게가 리스트로 입력
2. 한 보트의 무게제한도 입력이 됨.
3. 무게제한에 채워 최대한 적은 보트를 사용하도록 해야함.
    3-1. 양 끝에서 수를 합쳐서, limit 안에 들어가는지 확인.
        3-1-1. limit보다 작다면 
    3-2. 
'''
from collections import deque

def solution(people, limit):
    deq = deque(sorted(people))
    time = 0
    while len(deq) > 1:
        n = deq[0] + deq[-1]
        if n > limit:      
            time += 1
            deq.pop()
        else:
            time += 1
            deq.pop()
            deq.popleft()
    if len(deq) == 1:
        time += 1
    return time