import sys
max = int(0)
num = int(0)
for i in range(0, 9):
    input_a = int(sys.stdin.readline())
    if max < input_a:
        max = input_a
        num = i+1
print(max)
print(num)