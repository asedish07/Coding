import sys

list_n = []
n = int(sys.stdin.readline())
for i in range(n):
  num = int(sys.stdin.readline())
  list_n.append(num)
list_n.sort()
for i in range(n):
  print(list_n[i])