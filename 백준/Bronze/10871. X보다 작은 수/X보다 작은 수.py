import sys
n, s = map(int, sys.stdin.readline().split())
num = list(map(int, sys.stdin.readline().split()))
for i in range(0, n):
    if(num[i]<s):
        print("%d" %num[i], end=' ')