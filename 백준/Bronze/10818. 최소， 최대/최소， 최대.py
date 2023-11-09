import sys
n = int(sys.stdin.readline())
list_n = list(map(int, sys.stdin.readline().split()))
least = int(1000000)
biggest = int(-1000000)
for i in range(0, n):
    if list_n[i] > biggest:
        biggest = list_n[i]
    if list_n[i] < least:
        least = list_n[i]
print(least, biggest)