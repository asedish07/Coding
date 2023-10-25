import sys

x, y, w, h = map(int, sys.stdin.readline().split())
xw = int(w-x)
yh = int(h-y)
if (x<=xw and x<=y and x<=yh):
    print(x)
elif (y<=xw and y<=x and y<=yh):
    print(y)
elif (xw<=x and xw<=y and xw<=yh):
    print(xw)
else:
    print(yh)