# 행복 왕국의 왕실 정원은 체스판과 같은 8 x 8 좌표 평면이다. 왕실 정원의 특정한 한 칸에 나이트가 서 있다.
# 나이트는 이동을 할 때 L자 형태로만 이동할 수 있으며 정원 밖으로는 나갈 수 없다.
# 나이트는 특정한 위치에서 다음과 같은 2가지 경우로 이동할 수 있다
# 1. 수평으로 두 칸 이동한 뒤에 수직으로 한 칸 이동하기
# 2. 수직으로 두 칸 이동항 뒤에 수평으로 한 칸 이동하기
# 이처럼 8 x 8 좌표 평면상에서 나이트의 위치가 주어졌을 때 나이트가 이동할 수 있는 경우의 수를 출력하는 프로그램을 작성하시오
# 왕실 정원
#   a b c d e f g h
# 1
# 2
# 3
# 4
# 5
# 6
# 7
# 8
# 입력 예시
# a1
# 출력 예시
# 2
n = input()
location = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7, 'h': 8}
x = int(location[n[0]])
y = int(n[1])
roots = [(1, -2), (2, -1), (2, 1), (1, 2), (-1, 2), (-2, 1), (-2, -1), (-1, -2)]
result = 0

for root in roots:
    nx = x + root[0]
    ny = y + root[1]
    if 0 < nx <= 8 and 0 < ny <= 8:
        result += 1

print(result)

##### 답안 예시
input_data = input()
row = int(input_data[1])
# ord()는 문자의 유니코드 값을 돌려주는 함수이다.
column = int(ord(input_data[0])) - int(ord('a')) + 1
steps = [(-2, -1), (-1, -2), (1, -2), (2, -1), (2, 1), (1, 2), (-1, 2), (-2, 1)]
result = 0

for step in steps:
    next_row = row + step[0]
    next_column = column + step[1]
    if next_row >= 1 and next_row <= 8 and next_column >= 1 and next_column <= 8:
        result += 1

print(result)