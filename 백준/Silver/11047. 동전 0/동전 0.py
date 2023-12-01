import sys

n, v = map(int, sys.stdin.readline().split())
lst = []
cnt = 0
for i in range(n):
  lst.append(int(sys.stdin.readline()))
lst.reverse()
for i in range(n):
  a = v // lst[i]
  if a > 0:
    v -= lst[i] * a
    cnt += a
print(cnt)