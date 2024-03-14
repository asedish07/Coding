f, s = map(int, input().split())

f_factorial = 1
s_factorial = 1
fs_factorial = 1

for i in range(1, f + 1):
    f_factorial *= i

for i in range(1, s + 1):
    s_factorial *= i

fs = f - s
for i in range(1, fs + 1):
    fs_factorial *= i

print(f_factorial // (fs_factorial * s_factorial))
