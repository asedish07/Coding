import sys

N, M = map(int, sys.stdin.readline().split())
ball = []
for a in range(0, N):
    ball.append(a+1)
for i in range (0, M):
    f, s = map(int, sys.stdin.readline().split())
    stack = ball[f-1]
    ball[f-1] = ball[s-1]
    ball[s-1] = stack
for j in range(0, N):
    print(ball[j], end=' ')