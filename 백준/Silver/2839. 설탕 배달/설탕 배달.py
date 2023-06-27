import sys
n = int(sys.stdin.readline())
bos = int(0)

while n >= 0:
    if n % 5 == 0:    #5의 배수이면
        bos += (n / 5)    #5로 나눈 값 출력
        print(int(bos))    #소숫점 나오지 않게 int형으로 변환
        break
    n -= 3    #5의 배수가 될 때 까지 입력받은 수에서 -3
    bos += 1    #3개씩 나누듯이 3을 뺄 때마다 포대 횟수 1개 추가
else:
    print(-1)
#인터넷 보고 이해했습니다.