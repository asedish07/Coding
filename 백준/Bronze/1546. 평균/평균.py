import sys

num = int(sys.stdin.readline())
list_a = [0]*num
list_a = list(map(int, sys.stdin.readline().split()))
M = max(list_a)
average = float(0)
for j in range(0, num):
    average += (list_a[j] / M) * 100
print(average/num)