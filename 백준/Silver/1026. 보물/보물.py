import sys

n = int(sys.stdin.readline())
total = 0
A = list(map(int, sys.stdin.readline().split()))
B = list(map(int, sys.stdin.readline().split()))
B.sort(reverse=True)
A.sort()

for i in range(n):
    total += A[i]*B[i]
print(total)