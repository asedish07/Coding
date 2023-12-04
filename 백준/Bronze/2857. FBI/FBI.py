a = []
for i in range(5):
  a.append(input())
cnt = []
for i in range(len(a)):
  if 'FBI' in a[i]:
    cnt.append(i + 1)
if len(cnt) == 0:
  print("HE GOT AWAY!")
else:
  for i in cnt:
    print(i, end=" ")