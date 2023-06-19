a = int(input())
for i in range(a):
    b, c = input().split()
    test = ''
    for i in c:
        test += int(b) * i
    print(test)