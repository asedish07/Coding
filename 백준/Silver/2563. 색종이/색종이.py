import sys

lst = [[0 for _ in range(100)] for _ in range(100)]
n = int(sys.stdin.readline())
for _ in range(n):
  f, s = map(int, sys.stdin.readline().split())
  for i in range(f - 1, f + 9):
    lst[i][s - 1 : s + 9] = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
print(sum(sum(j) for j in lst))