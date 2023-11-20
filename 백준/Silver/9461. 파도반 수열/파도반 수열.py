import sys

def wavy(num):
  D = [0] * 100
  D[0] = 1
  D[1] = 1
  D[2] = 1
  D[3] = 2
  D[4] = 2
  for x in range(5, 100):
    D[x] = D[x - 1] + D[x - 5]
  return D[num -  1]

n = int(sys.stdin.readline())
for i in range(n):
  print(wavy(int(sys.stdin.readline())))