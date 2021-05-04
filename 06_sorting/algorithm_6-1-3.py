# 퀵 정렬(Quick Sort): 기준을 설정한 다음 큰 수와 작은 수를 교환한 후 리스트를 반으로 나누는 방식으로 동작
# 가장 많이 사용되는 알고리즘으로 퀵 정렬과 비교할 만큼 빠른 알고리즘으로는 병합 정렬이 있다.
# 퀵 정렬에서는 피벗(Pivot)이 사용된다. 큰 숫자와 작은 숫자를 교환할 때, 교환하기 위한 기준을 바로 피벗이라고 한다.
# 가장 대표적인 분할 방식은 호어 분할(Hoare Partition)방식이며 다음과 같은 규칙에 따라서 피벗을 설정한다.
# 리스트에서 첫 번째 데이터를 피벗으로 정한다.
# 피벗을 설정한 뒤에는 왼쪽에서부터 피벗보다 큰 데이터를 찾고, 오른쪽에서부터 피벗보다 작은 데이터를 찾는다.
# 그다음 큰 데이터와 작은 데이터의 위치를 서로 교환해준다. 이러한 과정을 반복하면 피벗에 대하여 정렬이 수행된다.
# 5 7 9 0 3 1 6 2 4 8
# (1 4 2 0 3) 5 (6 9 7 8)
# 0 1 (2 4 3) 5 6 (9 7 8)
# 0 1 2 (4 3) 5 6 (8 7) 9
# 0 1 2 3 4 5 6 7 8 9

array = [5, 7, 9, 0, 3, 1, 6, 2, 4, 8]

def quick_sort(array, start, end):
    # 원소가 1개인 경우 종료
    if start >= end:
        return
    # 피벗은 첫 번째 원소
    pivot = start
    left = start + 1
    right = end
    while left <= right:
        # 피벗보다 큰 데이터를 찾을 때까지 반복
        while left <= end and array[left] <= array[pivot]:
            left += 1
        # 피벗보다 작은 데이터를 찾을 때까지 반복
        while right > start and array[right] >= array[pivot]:
            right -= 1
        # 엇갈렸다면 작은 데이터와 피벗을 교체
        if left > right:
            array[right], array[pivot] = array[pivot], array[right]
        # 엇갈리지 않았다면 작은 데이터와 큰 데이터를 교체
        else:
            array[left], array[right] = array[right], array[left]
        # 분할 이후 왼쪽 부분과 오른쪽 부분에서 각각 정렬 수행
        quick_sort(array, start, right - 1)
        quick_sort(array, right + 1, end)


quick_sort(array, 0, len(array) - 1)
print(array)