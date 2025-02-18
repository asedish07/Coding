import sys

n = int(sys.stdin.readline())
n = list(map(int, sys.stdin.readline().split()))
answer = 0

prime = [True] * 1001
prime[0] = False
prime[1] = False

for i in range(2, int(1001**0.5)+1):
    if prime[i]:
        for j in range(i**2, 1001, i):
            prime[j] = False
            
for i in n:
    if prime[i]:
        answer += 1
print(answer)