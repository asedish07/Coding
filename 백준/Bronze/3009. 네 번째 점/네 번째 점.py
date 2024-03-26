a, b = map(int, input().split())
c, d = map(int, input().split())
e, f = map(int, input().split())
lst = []

if a == c:
    lst.append(e)
elif a == e:
    lst.append(c)
else:
    lst.append(a)

if b == d:
    lst.append(f)
elif b == f:
    lst.append(d)
else:
    lst.append(b)

print(lst[0], lst[1])