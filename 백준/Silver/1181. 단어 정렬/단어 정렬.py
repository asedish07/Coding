import sys

n = int(sys.stdin.readline())
arr = set()
for i in range(n):
  input_prob = input()
  arr.add(input_prob)
arr = list(arr)
arr.sort()
arr.sort(key=len)
for i in range(len(arr)):
  print(arr[i])