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

n, m = list(map(int, input().split()))
array = list(map(int, input().split()))

h = max(array) - 1
while True:
    rice_cake = 0
    for i in array:
        if i - h < 0:
            rice_cake += 0
        else:
            rice_cake += i - h
    if rice_cake < m:
        h -= 1
    else:
        break

print(h)