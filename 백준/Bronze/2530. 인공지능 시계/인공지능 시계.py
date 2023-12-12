h, m, s = map(int, input().split())
usesec = int(input())
s += int(usesec % 60)
if s >= 60:
  m += s // 60
  s = int(s % 60)
m += usesec // 60
if m >= 60:
  h += m // 60
  m = int(m % 60)
if h >= 24:
  h = h % 24
print(h, m, s)