t=int(input())
square=[]

def distance(n1,n2):
    return abs((n2[0]-n1[0])**2+abs(n2[1]-n1[1])**2)

for _ in range(t):
    square=[]
    for _ in range(4):
        a,b=map(int,input().split())
        square.append([a,b])
    square=sorted(square)

    if distance(square[0],square[1])==distance(square[0],square[2])==distance(square[1],square[3]) and distance(square[1],square[2])==distance(square[0],square[3]):
        print(1)
    else:
        print(0)
