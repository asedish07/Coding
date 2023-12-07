lst = []
for i in range(5):
  n = int(input())
  if n <= 40:
    n = 40
  lst.append(n)
print((lst[0]+lst[1]+lst[2]+lst[3]+lst[4])//5)