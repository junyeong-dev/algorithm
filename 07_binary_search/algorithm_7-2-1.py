# 전자 매장에는 부품이 n개 있다. 각 부품은 정수 형태의 고유한 번호가 있다.
# 어느 날 손님이 m개 종류의 부품을 대량으로 구매하겠다며 견적서를 요청했다.
# 이때 가게 안에 부품이 모두 있는지 확인하는 프로그램을 작성해보자.
# 부품이 있으면 yes, 없으면 no를 출력
# 입력 예시
# 5
# 8 3 7 9 2
# 3
# 5 7 9
# 출력 예시
# no yes yes

def binary_search(array, target, start, end):
    mid = (start + end) // 2
    if start > end:
        return 'no'
    if array[mid] > target:
        return binary_search(array, target, start, mid - 1)
    elif array[mid] < target:
        return binary_search(array, target, mid + 1, end)
    else:
        return 'yes'

n = int(input())
stocks = list(map(int, input().split()))
m = int(input())
parts = list(map(int, input().split()))

stocks.sort()

for part in parts:
    result = binary_search(stocks, part, 0, n - 1)
    print(result, end=' ')



# 답안 예시(계수 정렬)
# n(가게의 부품 개수)을 입력받기
n = int(input())
array = [0] * 1000001

# 가게에 있는 전체 부품 번호를 입력받아서 기록
for i in input().split():
    array[int(i)] = 1

# m(손님이 확인 요청한 부품 개수)을 입력받기
m = int(input())
# 손님이 확인 요청한 전체 부품 번호를 공백으로 구분하여 입력
x = list(map(int, input().split()))

# 손님이 확인 요청한 부품 번호를 하나씩 확인
for i in x:
    # 해당 부품이 존재하는지 확인
    if array[i] == 1:
        print('yes', end=' ')
    else:
        print('no', end=' ')