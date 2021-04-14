
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
