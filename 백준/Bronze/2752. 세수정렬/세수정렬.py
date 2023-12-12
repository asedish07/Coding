lst = [0] * 3
lst[0], lst[1], lst[2] = map(int, input().split())
lst.sort()
print(lst[0], lst[1], lst[2])