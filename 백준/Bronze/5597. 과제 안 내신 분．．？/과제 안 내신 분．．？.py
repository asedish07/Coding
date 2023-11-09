import sys

a = [0] * 30
for j in range(0, 28):
    input_a = int(sys.stdin.readline())
    a[input_a-1] = 1
for k in range(0, 30):
    if(a[k]==0):
        print(k+1)