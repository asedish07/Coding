import sys
from collections import deque, defaultdict

def dfs(root):
    visited[root - 1] = True
    print(root, end=" ")
    
    for i in graph[root]:
        if not visited[i - 1]:
            dfs(i)
            
def bfs(root):
    queue = deque([root])
    visited[root - 1] = True
    
    while queue:
        tmp = queue.popleft()
        print(tmp, end=" ")
    
        for i in graph[tmp]:
            if not visited[i - 1]:
                visited[i - 1] = True
                queue.append(i)
    
n, m, v = map(int, sys.stdin.readline().split())
graph = defaultdict(list)
for _ in range(m):
    first, second = map(int, sys.stdin.readline().split())
    graph[first].append(second)
    graph[second].append(first)
for key in graph:
    graph[key].sort()

visited = [False] * n
dfs(v)
print()

visited = [False] * n
bfs(v)

# https://ji-gwang.tistory.com/291 dfs 코드 참고