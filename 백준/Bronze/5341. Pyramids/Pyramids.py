while True:
    a = int(input())
    if a == 0:
        break
    sum = 0
    for i in range(1, a + 1):
        sum += i
    print(sum)