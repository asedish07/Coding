natural = set(range(1, 10001))
make = set()

for i in range(1, 10001):
    for j in str(i):
        i += int(j)
    make.add(i)

self = sorted(natural - make)
for i in self:
    print(i)