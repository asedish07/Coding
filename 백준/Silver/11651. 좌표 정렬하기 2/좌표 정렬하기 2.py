n = int(input())
lst = [list(map(int, input().split())) for _ in range(n)]
lst.sort(key=lambda x: (x[1], x[0]))
for f, s in lst:
    print(f, s)