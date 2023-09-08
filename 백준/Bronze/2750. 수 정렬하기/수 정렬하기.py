import sys

n = int(sys.stdin.readline())
list_a = [0] * n
for i in range(n):
  list_a[i] = int(sys.stdin.readline())
list_a = sorted(set(list_a))
for i in range(n):
  print(list_a[i])