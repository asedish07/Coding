n = int(input())
original_n = n
cnt = 0

while True:
    a = n // 10
    b = n % 10
    num = a + b
    new_num = b * 10 + num % 10
    cnt += 1
    if new_num == original_n:
        print(cnt)
        break
    n = new_num
