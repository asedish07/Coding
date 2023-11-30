import sys

n = int(sys.stdin.readline())
lst = list(map(int, sys.stdin.readline().split()))
lst.sort()

hap = 0
result = 0

for i in lst:
  result += (hap + i)
  hap += i
  
print(result)