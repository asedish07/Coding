import sys

n, m = map(int, sys.stdin.readline().split())
arr = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

# 2D prefix sum 배열 생성
prefix = [[0] * (m + 1) for _ in range(n + 1)]

# prefix 배열 채우기
for i in range(1, n + 1):
    for j in range(1, m + 1):
        prefix[i][j] = arr[i - 1][j - 1] + prefix[i - 1][j] + prefix[i][j - 1] - prefix[i - 1][j - 1]

# 질의 처리
q = int(sys.stdin.readline())
for _ in range(q):
    i, j, x, y = map(int, sys.stdin.readline().split())
    # 1-based 인덱스를 0-based로 바꾸어 계산
    total = prefix[x][y] - prefix[i - 1][y] - prefix[x][j - 1] + prefix[i - 1][j - 1]
    print(total)
