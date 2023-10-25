import sys

n = int(sys.stdin.readline())
for i in range(n):
    for k in range((n-1)-i):
        print(' ', end='')
    for j in range(2*i+1):
        print('*', end='')
    print("")

for i in range(1, n):
    for k in range(i):
        print(' ', end='')
    for j in range((n*2-1)-i*2):
        print('*', end='')
    print("")