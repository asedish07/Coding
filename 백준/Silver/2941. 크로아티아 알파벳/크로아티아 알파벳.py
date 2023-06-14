a_list = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
b = input()
for i in a_list:
    b = b.replace(i, 'a')
print(len(b))