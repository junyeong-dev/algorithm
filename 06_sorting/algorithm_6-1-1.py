# 정렬(Sorting): 데이터를 특정한 기준에 따라서 순서대로 나열하는 것
# 정렬 알고리즘은 이진 탐색의 전처리 과정이기도 하다.

# 선택 정렬(Selection Sort): 데이터가 무작위로 여러 개 있을 때,
# 이 중에서 가장 작은 데이터를 선택해 맨 앞에 있는 데이터와 바꾸고,
# 그다음 작은 데이터를 선택해 앞에서 두 번째 데이터와 바꾸는 과정을 반복
array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

for i in range(len(array)):
    # 가장 작은 원소의 인덱스
    min_index = i
    for j in range(i + 1, len(array)):
        if array[min_index] > array[j]:
            min_index = j
    # 스와프
    array[i], array[min_index] = array[min_index], array[i]

print(array)

# 스와프란 특정한 리스트가 주어졌을 때 두 변수의 위치를 변경하는 작업을 의미
# 파이썬에서는 다음처럼 간단히 변경할 수 있으나, 다른 언어에서는 임시 저장용 변수가 필요

# 0 인덱스와 1 인덱스의 원소 교체하기
array = [3, 5]
array[0], array[1] = array[1], array[0]

print(array)