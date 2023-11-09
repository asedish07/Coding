import sys

N, M = map(int, sys.stdin.readline().split())
index = []
for a in range(N):
    index.append(0)
for i in range(M):
    f, s, t = map(int, sys.stdin.readline().split()) #sys.stdin.readline() == input()
    for g in range(f-1, s):
        index[g] = t
for j in range(0, N):
    print(index[j], end=' ')