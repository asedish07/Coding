import sys

phone_number = sys.stdin.readline()
num = int(0)
for i in range((len(phone_number)) - 1):
    input_a = ord(phone_number[i])
    if input_a in range(65, 68):
        num += 2
    elif input_a in range(68, 71):
        num += 3
    elif input_a in range(71, 74):
        num += 4
    elif input_a in range(74, 77):
        num += 5
    elif input_a in range(77, 80):
        num += 6
    elif input_a in range(80, 84):
        num += 7
    elif input_a in range(84, 87):
        num += 8
    elif input_a in range(87, 91):
        num += 9
    else:
        num += 10
print(num + len(phone_number) - 1)