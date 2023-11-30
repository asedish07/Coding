import sys

check = 0
cnt = 0
lst = list(map(int, sys.stdin.readline().split()))
if lst[0] == 1:
  for i in range(1, 9):
    if lst[i - 1] == i:
      check += 1
  if check == 8:
    print('ascending')
    exit(0)
  else:
    check = 0
elif lst[0] == 8:
  for i in range(8, 0, -1):
    if lst[cnt] == i:
      check += 1
    cnt += 1
  if check == 8:
    print('descending')
    exit(0)
  else:
    check = 0
print('mixed')