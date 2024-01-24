n = int(input())
lst = list(map(int, input().split()))
num = 0
for i in lst:
    if i == n:
        num += 1
print(num)
