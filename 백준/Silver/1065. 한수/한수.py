n = int(input())

if n < 100:
    print(n)
elif n < 1000:
    a = 0
    for i in range(100, n+1):
        b = int(i)
        if (b%10-b//10%10) == (b//10%10-b//100):
            a += 1
    print(99+a)
else:
    print(144)