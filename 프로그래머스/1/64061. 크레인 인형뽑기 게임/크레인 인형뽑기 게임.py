'''
return 사라진 인형 개수
'''

def solution(board, moves):
    answer = 0
    s = []
    for i in moves:
        for j in range(0, len(board)):
            # tmp = board
            if board[j][i - 1] != 0:
                s.append(board[j][i-1])
                board[j][i-1] = 0
                break
        if len(s) >= 2:
            if s[len(s) - 1] == s[len(s) - 2]:
                s.pop()
                s.pop()
                answer += 2
    return answer