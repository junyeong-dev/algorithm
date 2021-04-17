# 게임 캐릭터가 맵 안에서 움직이는 시스템을 개발 중이다. 캐릭터가 있는 장소는 1 x 1 크기의 정사각형으로 이뤄진
# n x m 크기의 직사각형으로, 각각의 칸은 육지 또는 바다이다. 캐릭턴느 공서남북 중 한 곳을 바라본다.
# 캐릭터는 상하좌우로 움직일 수 있고, 바다로 되어 있는 공간에는 갈 수 없다. 움직임의 매뉴얼은 다음과 같다.
# 1. 현재 위치에서 현재 방향을 기준으로 왼쪽 방향(반시계 방향으로 90도 회전한 방향)부터 차례대로 갈 곳을 정한다.
# 2. 캐릭터의 바로 왼쪽 방향에 아직 가보지 않은 칸이 존재한다면, 왼쪽 방향으로 회전한 다음 왼쪽으로 한 칸을 전진한다.
#    왼쪽 방향에 가보지 않은 칸이 없다면, 왼쪽 방향으로 회전만 수행하고 1단계로 돌아간다.
# 3. 만약 네 방향 모두 이미 가본 칸이거나 바다로 되어 있는 칸인 경우에는, 바라보는 방향을 유지한 채로 한 칸 뒤로 가고
#    1단계로 돌아간다. 단, 이때 뒤쪽 방향이 바다인 칸이라 뒤로 갈 수 없는 경우에는 움직임을 멈춘다.
# 입력 예시
# 4 4       # 4 x 4 맵 생성
# 1 1 0     # (1, 1)에 북쪽(0)을 바라보고 서 있는 캐릭터
# 1 1 1 1   # 맵
# 1 0 0 1
# 1 1 0 1
# 1 1 1 1

# n, m을 공백으로 구분하여 입력받기
n, m = map(int, input().split())
# 현재 캐릭터의 x, y좌표, 방향을 각각 입력받기
# 북: 0, 동: 2, 남: 2, 서: 3
x, y, direction = map(int, input().split())
# 0: 육지, 1: 바다
game_map = [0 for _ in range(n)]
# 맴 정보 입력받기
for i in range(n):
    game_map[i] = list(map(int, input().split()))

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

result = 0
turn_time = 0

while True:
    if turn_time == 4:
        result += 1
        break
    if x + dx[direction] > n - 1 or y + dy[direction] > m - 1:
        direction -= 1
        turn_time += 1
        if direction == -1:
            direction = 3
        continue
    if game_map[x + dx[direction]][y + dy[direction]] == 1:
        direction -= 1
        turn_time += 1
        if direction == -1:
            direction = 3
        continue
    else:
        game_map[x][y] = 1
        x += dx[direction]
        y += dy[direction]
        result += 1
        turn_time = 0

print(result)
# 위에는 조금 빠진 부분이 있음
