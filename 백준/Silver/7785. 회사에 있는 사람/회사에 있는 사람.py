import sys

di = dict()
n = int(sys.stdin.readline())
name = ''
work = ''
for i in range(n):
  name, work = sys.stdin.readline().split()
  di[name] = work
d1 = sorted(di, reverse=True)
# di = d1
for i in d1:
  if di[i] == 'enter':
    print(i)