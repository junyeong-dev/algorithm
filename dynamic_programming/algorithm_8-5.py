# n가지 종류의 화폐가 있다. 이 화폐들의 개수를 최소한으로 이용해서 그 가치의 합이
# m원이 되도록 하려고 한다. 이때 각 화폐는 몇 개라도 사용할 수 있으며, 사용한 화폐의
# 구성은 같지만 순서만 다른 것은 같은 경우로 구분한다.
# 예를 들어 2원, 3원 단위의 화폐가 있을 때는 15원을 만들기 위해 3원을 5개 사용하는 것이
# 가장 최소한의 화폐 개수이다.
# 불가능할 때는 -1을 출력한다.
# 입력 예시 1
# 2 15
# 2
# 3
# 출력 예시 1
# 5

# 입력 예시 2
# 3 4
# 3
# 5
# 7
# 출력 예시 2
# -1

#

n, m = map(int, input().split())

array = []
for i in range(n):
    array.append(int(input()))

# 한 번 계산된 결과를 저장하기 위한 DP 체이블 초기화
d = [10001] * (m + 1)

# 다이나믹 프로그래밍(Dynamic Programming) 진행(버텀업)
d[0] = 0
for i in range(n):
    for j in range(array[i], m + 1):
        if d[j - array[i]] != 10001:
            d[j] = min(d[j], d[j - array[i]] + 1)

# 계산된 결과 출력
if d[m] == 10001:
    print(-1)
else:
    print(d[m])