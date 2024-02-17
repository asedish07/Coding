a, b, c = map(int, input().split())
f = a*b
if f < c:
    print(0)
else:
    print(f-c)