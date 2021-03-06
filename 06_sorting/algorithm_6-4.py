# 두 개의 배열 a와 b를 가지고 있다. 두 배열은 n개의 원소로 구성되어 있으며,
# 배열의 원소는 모두 자연수이다. 최대 k번의 바꿔치기 연산을 수행할 수 있으며,
# 바꿔치기 연산이란 배열 a에 있는 원소 하나와 배열 b에 있는 원소 하나를 골라서 두 원소를 서로
# 바꾸는 것을 말한다. 최종 목표는 a의 모든 원소의 합이 최대가 되도록 하는 것
# n, k 그리고 배열 a와 b의 정보가 주어졌을 때, 최대 k번의 바꿔치기 연산을 수행하여 만들 수 있는
# 배열 a의 모든 원소의 합이 최댓값을 출력하는 프로그램을 작성하시오.
# 예를 들어 n = 5, k = 3이고 배열 a와 b가 다음과 같다고 하자.
# 배열 a = [1, 2, 5, 4, 3]
# 배열 b = [5, 5, 6, 6, 5]
# 세 번의 연산 이후 배열 a와 b의 상태는 다음과 같이 구성될 것이다.
# 배열 a = [6, 6, 5, 4, 5]
# 배열 b = [3, 5, 1, 2, 5]
# 이때 배열 a의 모든 원소의 합은 26

n, k = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

for i in range(k):
    if min(a) < max(b):
        a[a.index(min(a))], b[b.index(max(b))] = b[b.index(max(b))], a[a.index(min(a))]
    else:
        break

print(sum(a))

# n과 k를 입력받기
n, k = map(int, input().split())
# 배열 a, b를 입력받기
a = list(map(int, input().split()))
b = list(map(int, input().split()))

# 배열 a는 오름차순 정렬
a.sort()
# 배열 b는 내림차순 정렬
b.sort(reverse=True)

# 첫 번째 인덱스부터 확인하며, 두 배열의 원소를 최대 k번 비교
for i in range(k):
    # a의 원소가 b의 원소보다 작은 경우
    if a[i] < b[i]:
        # 두 원소를 교체
        a[i], b[i] = b[i], a[i]
    # a의 원소가 b의 원소보다 크거나 같을 때, 반복문을 탈출
    else:
        break

# 배열 a의 모든 원소의 합을 출력
print(sum(a))