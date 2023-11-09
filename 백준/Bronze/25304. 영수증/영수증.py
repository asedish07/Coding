X = int(input())
number = int(input())
plus = 0
plus = int(plus)
for i in range(0, number):
    a, b = map(int, input().split())
    plus = plus + a*b
if plus==X:
    print('Yes')
else:
    print('No')