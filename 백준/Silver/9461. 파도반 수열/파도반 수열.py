import sys

lst = [1, 1, 1, 2, 2, 3, 4, 5, 7, 9]
n = int(sys.stdin.readline())
for i in range(10, 100):
  lst.append(lst[i - 1] + lst[i - 5])
for i in range(n):
  num = int(sys.stdin.readline())
  print(lst[num - 1])