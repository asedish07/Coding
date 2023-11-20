import sys

def fib(num):
  D = [0] * 40
  D[0] = 1
  D[1] = 1
  for i in range(2, 40):
    D[i] = D[i - 1] + D[i - 2]
  return D[num - 1]

n = int(sys.stdin.readline())
tmp = fib(n)
print(tmp, n - 2)