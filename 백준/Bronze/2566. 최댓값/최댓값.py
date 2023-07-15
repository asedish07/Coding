list_a = [list(map(int, input().split())) for _ in range(9)]
max = int(0)
m_r = int(0)
m_c = int(0)
for i in range(9):
    for j in range(9):
        if list_a[i][j] >= max:
            max = list_a[i][j]
            m_r = i + 1
            m_c = j + 1
print(max)
print(m_r, m_c)