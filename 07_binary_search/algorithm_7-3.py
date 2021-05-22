# 길이가 일정하지 않는 떡을 절단기로 자른다.
# 절단기에 높이(h)를 지정하면 줄지어진 떡을 한 번에 절단한다.
# 높이가 h보다 긴 떡은 h 위의 부분이 잘릴 것이고, 낮은 떡은 잘리지 않는다.
# 예를 들어 높이가 19, 14, 10, 17cm인 떡이 나란히 있고 절단기 높이를 15cm로
# 지정하면 자른 뒤 떡의 높이는 15, 14, 10, 15cm가 될 것이다.
# 잘린 떡의 길이는 차례대로 4, 0, 0, 2cm이다. 손님은 6cm만큼의 길이를 가져간다.
# 손님이 왔을 때 요청한 총 길이가 m일 때 적어도 m만큼의 떡을 얻기 위해 절단기에 설정할 수 있는
# 높이의 최댓값을 구하는 프로그램을 작성하시오.
# 입력 예시
# 4 6
# 19 15 10 17
# 출력 예시
# 15

# 떡의 개수(n)와 요청한 떡의 길이(m)을 입력받기
n, m = list(map(int, input().split()))
# 각 떡의 개별 높이 정보를 입력받기
array = list(map(int, input().split()))

# h = max(array) - 1
# while True:
#     rice_cake = 0
#     for i in array:
#         if i - h < 0:
#             rice_cake += 0
#         else:
#             rice_cake += i - h
#     if rice_cake < m:
#         h -= 1
#     else:
#         break
#
# print(h)
# >> 탐색 범위의 따라 시간 초과 가능성이 높다
# 그러므로 이진 탐색으로 해결해야 함

# 답변 예시
# 이진 탐색을 위한 시작점과 끝점 설정
start = 0
end = max(array)

# 이진 탐색
result = 0
while start <= end:
    total = 0
    mid = (start + end) // 2
    for x in array:
        # 잘랐을 떄의 떡의 양 계산
        if x > mid:
            total += x - mid
    # 떡의 양이 부족한 경우 더 많이 자르기(왼쪽 부분 탐색)
    if total < m:
        end = mid - 1
    # 떡의 양이 충분한 경우 덜 자르기(오른쪽 부분 탐색)
    else:
        # 최대한 덜 잘랐을 때가 정답이므로, 여기에서 result에 기록
        result = mid
        start += 1

print(result)