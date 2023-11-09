import sys
r = int(input())
n = list(map(int, sys.stdin.readline().split()))
v = int(sys.stdin.readline())
cunt = int(0)
for j in range(0, r):
    if v == n[j]:
        cunt += 1
print(cunt)