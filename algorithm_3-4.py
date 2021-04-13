# 어떠한 수 n이 1이 될 때까지 다음의 과정 중 하나를 반복적으로 선택하여 수행
# 단 2번째 연산은 n이 k로 나누어떨어질 때만 선택할 수 있다
# 1. n에서 1을 뺀다
# 2. n을 k로 나눈다
# n이 1이 될 때까지 1번 혹은 2번의 과정을 수행해야 하는 최소 횟수를 구하시오
# 입력 예시
# 25 5
# 출력 예시
# 2

# n, k를 공백으로 구분하여 입력받기
n, k = map(int, input().split())
result = 0

while True:
    if n % k == 0:
        n /= k
    else:
        n -= 1
    result += 1
    if n == 1:
        break

print(result)
