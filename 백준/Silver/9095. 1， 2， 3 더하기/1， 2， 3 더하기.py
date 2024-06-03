import sys

n = int(sys.stdin.readline())
lst = [0] * 10
lst[0] = 1
lst[1] = 2
lst[2] = 4
for i in range(3, 10):
  lst[i] = lst[i - 1] + lst[i - 2] + lst[i - 3]
for i in range(n):
  num = int(sys.stdin.readline())
  print(lst[num - 1])