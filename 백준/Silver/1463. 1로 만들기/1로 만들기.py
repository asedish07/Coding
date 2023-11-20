import sys

N = int(sys.stdin.readline())

def Fibonacci_td(num):
  D = [0] * (num + 1)
  
  for i in range(2, N + 1):
    D[i] = D[i - 1] + 1
    if i % 2 == 0:
      D[i] = min(D[i], D[i//2] + 1)
    if i % 3 == 0:
      D[i] = min(D[i], D[i//3] + 1)
  return D[num]

print(Fibonacci_td(N))