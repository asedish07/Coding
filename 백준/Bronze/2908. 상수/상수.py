#이름 바꾸기 위해서는 Pycharm에서 Shift+F6을 눌러야 함

a, b = input().split()
a = a[::-1]
b = b[::-1]

print(max(a, b))