t, m = map(int, input().split())
ft = int(input())
t += (ft + m) // 60
m = (ft+m) % 60
if t >= 24:
  t -= 24
print(f"{t} {m}")