# 삽입 정렬(Insertion Sort): 특정한 데이터를 적절한 위치에 갑입한다는 의미
# 특정한 데이터가 적절한 위치에 들어가기 이전에, 그 앞까지의 데이터는 이미 정렬되어 있다고 가정
# 정렬되어 있는 데이터 리스트에서 적절한 위치를 찾은 뒤에, 그 위치에 삽입된다는 점이 특징
array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

for i in range(1, len(array)):
    # 인덱스 i부터 1까지 감소하며 반복하는 문법
    for j in range(i, 0, -1):
        # 한 칸씩 왼쪽으로 이동
        if array[j] < array[j - 1]:
            array[j], array[j - 1] = array[j - 1], array[j]
        # 자기보다 작은 데이터를 만나면 그 위치에서 멈춤
        else:
            break

print(array)