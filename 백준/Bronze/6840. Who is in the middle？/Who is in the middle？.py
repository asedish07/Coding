import sys

a = int(sys.stdin.readline())
b = int(sys.stdin.readline())
c = int(sys.stdin.readline())
if (a >= b and c >= a) or (a >= c and b >= a):
  print(a)
elif (b >= a and b <= c) or (b >= c and b <= a):
  print(b)
else:
  print(c)