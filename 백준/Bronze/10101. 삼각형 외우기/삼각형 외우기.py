import sys

a = int(sys.stdin.readline())
b = int(sys.stdin.readline())
c = int(sys.stdin.readline())
s = a+b+c
if a == b and b == c and a == 60:
    print("Equilateral")
elif (a == b or b == c or a == c) and s == 180:
    print("Isosceles")
elif s == 180:
    print("Scalene")
else:
    print("Error")