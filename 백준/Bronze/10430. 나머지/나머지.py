a, b, c = input().split()
a = int(a)
b = int(b)
c = int(c)
d = (a+b)%c
e = ((a%c)+(b%c))%c
f = (a*b)%c
g = ((a%c)*(b%c))%c
print("%d\n%d\n%d\n%d" %(d, e, f, g))