import sys

n = int(sys.stdin.readline())
if n == 1:
  print(int(sys.stdin.readline()))
  exit(0)
elif n == 2:
  a1 = int(sys.stdin.readline())
  a2 = int(sys.stdin.readline())
  print(a1+a2)
else:
  num_lst = list(int(sys.stdin.readline()) for _ in range(n))
  dptable = [0] * n
  dptable[0] = num_lst[0]
  dptable[1] = num_lst[0] + num_lst[1]
  dptable[2] = max(num_lst[0] + num_lst[2], num_lst[1] + num_lst[2])
  for i in range(3, n):
    dptable[i] = max(dptable[i-2] + num_lst[i], dptable[i-3]+ num_lst[i-1] + num_lst[i])
  print(dptable[n - 1])