import sys

stack = []

def push(num):
  stack.append(num)

def popp():
  if stack:
    return stack.pop()
  else:
    return -1

def peek():
  return stack[-1]

n = int(sys.stdin.readline())
for i in range(n):
  a = sys.stdin.readline().split()
  if a[0] == 'push':
    push(a[1])
  elif a[0] == 'pop':
    print(popp())
  elif a[0] == 'size':
    print(len(stack))
  elif a[0] == 'empty':
    if not stack:
      print(1)
    else:
      print(0)
  else:
    if not stack:
      print(-1)
    else:
      print(peek())