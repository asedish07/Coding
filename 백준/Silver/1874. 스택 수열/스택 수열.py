N = int(input())
stack = []
op = []
count = 1

for _ in range(N):
    num = int(input())

    # count가 num보다 작거나 같으면 그 사이의 숫자들을 모두 스택에 넣기
    while count <= num:
        stack.append(count)
        op.append('+')
        count += 1

    # 스택의 마지막 값이 num과 같으면 pop하고 '-' 연산 기록
    if stack and stack[-1] == num:
        stack.pop()
        op.append('-')
    else:
        print("NO")
        break
else:
    # 정상적으로 모든 연산을 마친 경우
    print("\n".join(op))
