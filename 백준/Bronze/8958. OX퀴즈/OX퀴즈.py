import sys

cnt = 0
point = 0
n = int(sys.stdin.readline())
for i in range(n):
  char = input()
  for j in char:
    if j == 'O':
      cnt += 1
      point += cnt
    else:
      cnt = 0
  print(point)
  point = 0
  cnt = 0