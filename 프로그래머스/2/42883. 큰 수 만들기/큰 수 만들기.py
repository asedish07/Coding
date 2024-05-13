# k개 만큼의 숫자를 골라 가장 작은 수를 만들고, 빼자
# 

def solution(number, k):
    answer = ''
    answer = number[-(k-1):]
    tmp = list(number[:-(k-1)])
    while len(tmp) == k-1:
        ma = tmp.index(max(tmp))
        
     return answer