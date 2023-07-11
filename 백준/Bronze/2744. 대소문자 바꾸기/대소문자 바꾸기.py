input_a = input()
for i in input_a:
    if i >= "a" and i <= 'z':
        print(chr(ord(i)-32), end="")
    else:
        print(chr(ord(i)+32), end='')