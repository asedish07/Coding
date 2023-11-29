lst = []
top = -1
check = 0

n = int(input())
for i in range(n):
  ipt = input()
  for j in ipt:
    if j == '(':
      top += 1
    elif top == -1 and j == ')':
      check += 1
    else:
      top -= 1
  if check != 0:
    print("NO")
  elif top == -1:
    print("YES")
  else:
    print("NO")
  top = -1
  check = 0