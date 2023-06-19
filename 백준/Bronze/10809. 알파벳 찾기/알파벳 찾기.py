S = list(input())
le = [-1] * 26
count = int(0)
for i in S:
    if le[ord(i)-97] == -1:
        le[ord(i)-97] = count
    count += 1
for i in range(0, 26):
    print(le[i], end=" ")