L = int(input())
a = int(input())
b = int(input())
c = int(input())
d = int(input())
left_k = a//c
left_m = b//d
if a%c != 0:
    left_k += 1
if b%d != 0:
    left_m += 1
L_k = L - left_k
L_m = L - left_m
if L_k < L_m:
    print(L_k)
elif L_m < L_k:
    print(L_m)
else:
    print(L_k)