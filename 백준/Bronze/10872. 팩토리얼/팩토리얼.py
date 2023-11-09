import sys

n = int(sys.stdin.readline())
a = int(1)
for i in range(1, n+1):
    a *= i
if n==0:
    print(1)
else:
    print(a)