import sys

n = int(sys.stdin.readline())
for i in range(n):
    cnt = 0
    lst = list(map(int, sys.stdin.readline().split()))
    numbers = list(lst[1:])
    avg = sum(numbers)/lst[0]
    for i in numbers:
        if i > avg:
            cnt += 1
    print(f"{round(cnt/lst[0] * 100, 3)}%")