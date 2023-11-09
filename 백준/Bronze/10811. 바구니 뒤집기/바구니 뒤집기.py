import sys

n, m = map(int, sys.stdin.readline().split())
list_a = [a for a in range(1, n+1)]
for b in range(0, m):
    i, j = map(int, sys.stdin.readline().split())
    list_a[i-1:j] = reversed(list_a[i-1:j])
for k in range(0, n):
    print(list_a[k], end=' ')