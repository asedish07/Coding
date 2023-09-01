list_a = [input() for _ in range(5)]
for i in range(15):
    for j in range(5):
        if len(list_a[j]) > i:
            print(list_a[j][i], end='')