import sys
a = sys.stdin.readline()
a = int(a)
for i in range(0, a):
    b, c = map(int, sys.stdin.readline().split())
    print(b+c)