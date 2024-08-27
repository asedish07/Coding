from collections import deque
import sys

n = int(sys.stdin.readline())
queue = deque([x for x in range(n, 0, -1)])
while len(queue) != 1:
    queue.pop()
    tmp = queue.pop()
    queue.appendleft(tmp)
print(queue[0])