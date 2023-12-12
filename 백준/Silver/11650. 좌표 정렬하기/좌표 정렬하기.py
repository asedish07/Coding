lst = []
n = int(input())
for i in range(n):
  f, s = map(int, input().split())
  lst.append([f, s])
lst.sort()
for i, j in lst:
  print(i, j)