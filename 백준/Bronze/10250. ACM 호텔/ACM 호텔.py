import sys

lst = []
n = int(sys.stdin.readline())
for i in range(n):
    h, w, n = map(int, sys.stdin.readline().split())
    floor = n % h if n % h != 0 else h
    room_number = (n - 1) // h + 1
    room = floor * 100 + room_number
    lst.append(room)

for j in lst:
    print(j)
