import sys

n, m = map(int, sys.stdin.readline().split())
t = n + m

dic = {}
lst = []
number = 0

for _ in range(t):
    tmp = sys.stdin.readline().strip()
    try:
        dic[tmp] += 1
    except:
        dic[tmp] = 1

for k, v in dic.items():
    if v == 2:
        number += 1
        lst.append(k)

print(number)

print("\n".join(sorted(lst)))