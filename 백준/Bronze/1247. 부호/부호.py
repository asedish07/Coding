import sys

timesum = 0
for i in range(3):
    n = int(sys.stdin.readline())
    lst = [int(sys.stdin.readline()) for _ in range(n)]
    tmp = sum(lst)
    if tmp < 0:
        print("-")
    elif tmp == 0:
        print("0")
    else:
        print("+")