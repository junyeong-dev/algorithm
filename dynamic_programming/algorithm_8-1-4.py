# 재귀 함수를 사용하면 컴퓨터 시스템에서는 함수를 다시 호출했을 때 메모리 상에
# 적재되는 일련의 과정을 따라야 하므로 오버헤드가 발생할 수 있다.
# 따라서 재귀 함수 대신에 반복문을 사용하여 오버헤드를 줄일 수 있다.
# 일반적으로 반복문을 이용한 다이나믹 프로그래밍이 더 성능이 좋기 때문이다.
# 반복문을 이용하여 소스코드를 작성하는 경우 작은 문제부터 차근차근 답을
# 도출한다고 하여 보텀업(Bottom-Up) 방식이라고 말한다.

# 탑다운(메모이제이션) 방식은 '하향식'이라고도 하며, 보텀업 방식은 '상향식'이라고도 한다.
# 다이나믹 프로그래밍의 전형적인 형태는 보텀업 방식이다.
# 보텀업 방식에서 사용되는 결과 저장용 리스트는 'DP 테이블'이라고 부르며,
# 메모이제이션은 탑다운 방식에 국한되어 사용되는 표현이다.

# 앞서 계산된 결과를 저장하기 위한 DP 테이블 초기화
d = [0] * 100

# 첫 번째 피보나치 수와 두 번째 피보나치 수는 1
d[1] = 1
d[2] = 1
n = 99

# 피보나치 함수(Fibonacci Function) 반복문으로 구현(보텀업 다이나믹 프로그래밍)
for i in range(3, n - 1):
    d[i] = d[i - 1] + d[i - 2]

print(d[n])