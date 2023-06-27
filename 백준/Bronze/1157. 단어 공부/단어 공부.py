a = input()
n = len(a)
arr = [0]*91
for i in range(0, n):
    c = ord(a[i])
    if c >= 91:
        c -= 32
    arr[c] += 1
biggest = int(0)
biggestn = int(0)
for i in range(65, 91):
    if biggest < arr[i]:
        biggest = arr[i]
        biggestn = i
cnt = int(0)
for i in range(65, 91):
    if biggestn != i:
        if biggest == arr[i]:
            cnt += 1
if cnt >= 1:
    print("?")
else:
    print(chr(biggestn))