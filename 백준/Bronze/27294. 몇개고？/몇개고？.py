import sys

t, s = map(int, sys.stdin.readline().split())
if 12 <= t <= 16 and s == 0:
  print(320)
else:
  print(280)