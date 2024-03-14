n = int(input())
cnt = 0
num = 666

while True:
    if '666' in str(num):
        cnt += 1
    if cnt == n:
        break
    num += 1
print(num)
# 문제 이해는 인터넷 참고