
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