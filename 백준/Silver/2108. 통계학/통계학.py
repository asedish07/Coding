import sys

n = int(sys.stdin.readline())
lst = []
count = {}
for _ in range(n):
    lst.append(int(sys.stdin.readline()))
print(round(sum(lst)/len(lst)))
print(sorted(lst)[n//2])
for i in lst:
    try:
        count[i] += 1
    except:
        count[i] = 1
maximum = []
m = max(count.values())
for k in count:
    if count[k] == m:
        maximum.append(k)
if len(maximum) == 1:
    print(maximum[0])
else:
    print(sorted(maximum)[1])
print(max(lst) - min(lst))