import sys

a = int(sys.stdin.readline())
num = int(a/5)
for i in range(0, num):
    print('V', end='')
n = int(a-num*5)
for j in range(0, n):
    print('I', end='')