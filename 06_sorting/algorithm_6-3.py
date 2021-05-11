# n명의 학생 정보가 있다. 학생 정보는 학생의 이름과 학생의 성적으로 구분된다.
# 각 학생의 이름과 성적 정보가 주어졌을 때 성적이 낮은 순서대로 학생의 이름을 출력하는
# 프로그램을 작성하시오
# 입력 예시
# 2
# 홍길동 95
# 이순신 77

# 출력 예시
# 이순신 홍길동

# n을 입력받기
n = int(input())

# n명의 학생 정보를 입력받아 리스트에 저장
array = []
for i in range(n):
    input_data = input().split()
    # 이름은 문자열, 점수는 정수형으로 저장
    array.append((input_data[0], int(input_data[1])))

# 키(key)를 이용하여, 점수를 기준으로 정렬
result = sorted(array, key=lambda array: array[1])

# 결과를 출력
for i in result:
    print(i[0], end=' ')