# 반복문으로 구현한 이진 탐색
def binary_search(array, target, start, end):
    while True:
        mid = (start + end) // 2
        if start > end:
            return print('원소가 존재하지 안습니다.')
        if array[mid] > target:
            end = mid - 1
        elif array[mid] < target:
            start = mid + 1
        else:
            return print(mid)

# n(원소의 개수)과 target(찾고자 하는 문자열)을 입력받기
n, target = list(map(int, input().split()))
# 전체 원소 입력받기
array = list(map(int, input().split()))

binary_search(array, target, 0, n - 1)

def binary_search2(array, target, start, end):
    while start <= end:
        mid = (start + end) // 2
        if array[mid] == target:
            return mid
        elif array[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
        return None

result = binary_search2(array, target, 0, n - 1)
if result == None:
    print('원소가 존재하지 안습니다.')
else:
    print(result + 1)