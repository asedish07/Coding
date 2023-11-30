import sys

a = int(sys.stdin.readline())
b = int(sys.stdin.readline())
c = int(sys.stdin.readline())
gob = list(str(a*b*c))
lst = [0] * 10
for i in gob:
  lst[int(i)] += 1
for i in lst:
  print(i)