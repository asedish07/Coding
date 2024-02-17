import sys

a, b = map(int, sys.stdin.readline().split())
lst = list(map(int, sys.stdin.readline().split()))
for i in lst:
    print(i-(a*b), end=" ")