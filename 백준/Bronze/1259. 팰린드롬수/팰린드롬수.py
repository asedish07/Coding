while True:
    ip = input()
    if ip == '0':
        break
    n = len(ip)
    cnt = 0
    for i in range(n):
        if ip[i] == ip[-i - 1]:
           cnt += 1
    if cnt == n:
        print('yes')
    else:
        print('no')