array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

# sorted() 함수
# 퀵 정렬과 동작 방식이 비슷한 병합 정렬을 기반으로 만들어짐
# 리스트, 딕셔너리 자료형 등을 입력받아 정렬된 결과를 출력
# 반환되는 결과는 리스트 자료형
result = sorted(array)
print(result)

# 리스트 객체의 내장 함수인 sort()는 별도의 정렬된 리스트가 반환되지 않고
# 내부 원소가 바로 정렬된다.
array.sort()
print(array)