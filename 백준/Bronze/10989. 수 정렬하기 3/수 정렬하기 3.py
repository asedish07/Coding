import sys

n = int(sys.stdin.readline())
n_list = [0] * 10000

for i in range(n):
  num = int(sys.stdin.readline())
  n_list[num - 1] += 1

for i in range(10000):
  if n_list[i] != 0:
    for j in range(n_list[i]):
      print(i + 1)