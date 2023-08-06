import sys
score = sys.stdin.readline()

# if score=='A+':
#     print(4.3)
# elif score=='A0':
#     print(4.0)
# elif score==''

# 계속 if문 쓰려다가 다르게 해보고 싶어서 바꿈

first = 0
second = 0

if score[0] == 'A':
    first = 4
elif score[0] == 'B':
    first = 3
elif score[0] == 'C':
    first = 2
else:
    first = 1

if score[1] == '+':
    second = 3
elif score[1] == '0':
    second = 0
else:
    second = 7

if second == 7:
    first -= 1

if score[0] == 'F':
    first = 0
    second = 0

print("%d.%d" %(first, second))