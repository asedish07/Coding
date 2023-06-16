# 행렬 크기 입력 받기
N, M = map(int, input().split())

# 첫 번째 행렬 입력 받기
matrix1 = []
for _ in range(N):
    row = list(map(int, input().split()))
    matrix1.append(row)

# 두 번째 행렬 입력 받기
matrix2 = []
for _ in range(N):
    row = list(map(int, input().split()))
    matrix2.append(row)

# 행렬 덧셈 수행
result = []
for i in range(N):
    row = []
    for j in range(M):
        sum_value = matrix1[i][j] + matrix2[i][j]
        row.append(sum_value)
    result.append(row)

# 결과 출력
for row in result:
    print(' '.join(map(str, row)))
