a = input()
b = input()
a = int(a)
b = int(b)
n4 = b%10 #두번째 입력받은 수의 1의 자리 수
n5 = (b%100)-n4 #두번째 입력받은 수의 10의 자리 수
n6 = b-n5-n4
print("%d\n%d\n%d\n%d" %(a*n4, a*n5/10, a*n6/100, a*b))
