import sys

n, m = map(int, sys.stdin.readline().split())

prime = [True] * (1000001)
prime[0] = prime[1] = False

for i in range(2, int(1000001**0.5) + 1):
    if prime[i]:
        for j in range(i * i, 1000001, i):
            prime[j] = False

for i in range(n, m + 1):
    if prime[i]:
        print(i)