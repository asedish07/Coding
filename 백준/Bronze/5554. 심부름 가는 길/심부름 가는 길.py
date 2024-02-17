time = int(input())
for _ in range(3):
    time += int(input())
minute = int(time // 60)
second = int(time % 60)
print(minute)
print(second)