# 수열을 내림차순으로 정렬하는 프로그램
# 입력 예시
# 3
# 15
# 27
# 12

# 출력 예시
# 27 15 12

# n을 입력받기
n = int(input())

# n개의 정수를 입력받아 리스트에 저장
array = []
for i in range(n):
    array.append(int(input()))

array.sort(reverse=True)

for i in array:
    print(i, end=" ")