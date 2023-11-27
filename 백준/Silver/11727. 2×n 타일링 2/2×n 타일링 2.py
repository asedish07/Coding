n = int(input())
lst = [0] * 1000
lst[0] = 1
lst[1] = 3
for i in range(2, 1000):
  lst[i] = lst[i-1]+2*lst[i-2]
print(lst[n - 1] % 10007)