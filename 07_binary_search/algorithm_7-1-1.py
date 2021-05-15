# 순차 탐색(Sequential Search): 리스트 안에 있는 특정한 데이터를 찾기 위해 앞에서 부터
# 데이터를 하나씩 차례대로 확인하는 방법
# 리스트 자료형에서 특정한 값을 가지는 원소의 개수를 세는 count() 메서드도 순차 탐색이 수행된다.

# 순차 탐색 소스코드 구현
def sequential_search(n, target, array):
    # 각 원소를 하나씩 확인
    for i in range(n):
        # 현재의 원소가 찾고자 하는 원소와 동일한 경우
        if array[i] == target:
            # 현재의 위치 반환(인덱스는 0부터 시작하므로 1 더하기)
            return i + 1

print("생성할 원소 개수를 입력한 다음 한 칸 띄고 찾을 문자열을 입력하세요.")
input_data = input().split()
# 원소의 개수
n = int(input_data[0])
# 찾고자 하는 문자열
target = input_data[1]

print("앞서 적은 원소 개수만큼 문자열을 입력하세요. 구분은 띄어쓰기 한 칸으로 합니다.")
array = input().split()

# 순차 탐색 수행 결과 출력
print(sequential_search(n, target, array))