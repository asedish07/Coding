import sys
import math

a, b = map(int, sys.stdin.readline().split())
for _ in range(math.gcd(a, b)):
    print(1, end="")