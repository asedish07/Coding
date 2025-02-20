import sys
from collections import deque

queue = deque()
for _ in range(int(sys.stdin.readline())):
    command = list(sys.stdin.readline().split())
    if command[0] == "push":
        queue.append(command[1])
    elif command[0] == "pop":
        if not queue:
            print(-1)
        else:
            print(queue.popleft())
    elif command[0] == "size":
        print(len(queue))
    elif command[0] == "empty":
        print(bool(not len(queue))*1)
    elif command[0] == "front":
        if not queue:
            print(-1)
        else:
            print(queue[0])
    else:
        if not queue:
            print(-1)
        else:
            print(queue[-1])