# 숫자가 쓰인 카드들이 n x m 형태로 놓여 있다 (n은 행의 개수, m은 열의 개수)
# 먼저 뽑고자 하는 카드가 포함되어 있는 행을 선택
# 그다음 선택된 행에 포한된 카드들 중 가장 숫자가 낮은 카드를 뽑아야 한다
# 따라서 처음에 카드를 골라낼 행을 선택할 때, 이후에 해당 행에서 가장 숫자가 낮은 카드를 뽑을
# 것을 고려하여 최종적으로 가장 높은 숫자의 카드를 뽑을 수 있도록 전략을 세워야 한다

# 입력 예시
# 3 3
# 3 1 2
# 4 1 4
# 2 2 2

# 출력 예시
# 2

# n, m을 공백으로 구분하여 입력받기
n, m = map(int, input().split())
result = 0

# 한줄 씩 입력받으면서 확인
for i in range(n):
    data = list(map(int, input().split()))
    minValue = min(data)
    if result < minValue:
        result = minValue

print(result)