# 예제 4-1-1
# 여행가 A는 n x n 코기의 정사각형 공간 위에 서 있다. 이 공간은 1 x 1 크기의 정사각형으로 나누어져 있다.
# 가장 왼쪽 위 좌표는 (1, 1)이며, 가장 오른쪽 아래 좌표는 (n, n)에 해당한다. 여행가는 상, 하, 좌, 우 방향으로
# 이동할 수 있으며, 시작 좌표는 항상 (1, 1)이다. 우리 앞에는 여행가 A가 이동할 계획이 적힌 계획서가 놓여 있다.
# 계획서에는 하나의 줄에 띄어쓰기를 기준으로 하여 L, R, U, D 중 하나의 문자가 반복적으로 적혀있다.
# L: 왼쪽으로 한 칸 이동
# R: 오른쪽으로 한 칸 이동
# U: 위쪽으로 한 칸 이동
# D: 아래쪽으로 한 칸 이동
# 이때 여행가 A가 n x n 크기의 정사각형 공간을 벗어나는 움직임은 무시된다. 예를 들어 (1, 1)의 위치에서
# L혹은 U를 만나면 무시된다.
# 입력 예시
# 5
# R R R U D D
# 출력 예시
# 3 4

# 공간의 크기
n = int(input())
# 이동 계획
move = input().split()
x, y = 1, 1

for i in move:
    tempX = x
    tempY = y
    if i == "R":
        tempY += 1
    elif i == "L":
        tempY -= 1
    elif i == "D":
        tempX += 1
    elif i == "U":
        tempX -= 1

    if 0 < tempX <= n:
        x = tempX
    if 0 < tempY <= n:
        y = tempY

print(x, y)

# 답안 예시
n = int(input())
plans = input().split()
x, y = 1, 1

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
moveTypes = ['L', 'R', 'U', 'D']

for plan in plans:
    for i in range(len(moveTypes)):
        if plan == moveTypes[i]:
            nx = x + dx[i]
            ny = y + dy[i]
    if nx < 1 or ny < 1 or nx > n or ny > n:
        continue
    x, y = nx, ny

print(x, y)

# 예제 4-1-2
# 정수 n이 입력되면 00시 00분 00초부터 n시 59분 59초까지의 모든 시각 중에서 3이 하나라도 포함되는 모든
# 경우의 수를 구하는 프로그램을 작성하시오
# 입력 예시
# 5
# 출력 예시
# 11475

n = int(input())
result = 0

for h in range(n+1):
    for m in range(60):
        for s in range(60):
            if '3' in str(h) + str(m) + str(s):
                result += 1

print(result)