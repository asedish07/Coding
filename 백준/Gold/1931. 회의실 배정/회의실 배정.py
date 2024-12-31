import sys

beforeend = 0
count = 0

lst = []
for _ in range(int(sys.stdin.readline())):
    lst.append(list(map(int, sys.stdin.readline().split())))
lst.sort(key=lambda x: (x[1], x[0]))

for start, end in lst:
    if beforeend <= start:
        count += 1
        beforeend = end
print(count)