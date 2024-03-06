n = input()
t = len(n) // 10
for i in range(t):
  print(n[(i*10):(i*10+10)])
print(n[t*10:])