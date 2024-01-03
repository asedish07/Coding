import sys

n = int(sys.stdin.readline())
people = []

for i in range(n):
    age, name = sys.stdin.readline().split()
    age = int(age)
    people.append((age, name))

people.sort(key=lambda x: x[0])

for person in people:
    print(person[0], person[1])
