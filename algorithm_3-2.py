# 배열에서 가장 큰 합을 구하는 알고리즘
# n : 배열의 개수, m : 총 더할 횟수, k : 최대 연속으로 더할 수 있는 횟수
# 예) n, m, k가 각각 5, 8, 3 배열은 2 4 5 4 6일 경우
# 총 더할 횟수는 8, 연속으로 더할 수 있는 횟수는 3
# 따라서 가장 큰수인 6을 3번 더한 후 그 다음 큰수인 5를 한번 더 하는 것을 반복
# 6 + 6 + 6 + 5 + 6 + 6 + 6 + 5 = 46

# n, m, k를 공백으로 구분하여 입력받기
n, m, k = map(int, input().split())
# n개의 수를 공백으로 구분하여 입력받기
data = list(map(int, input().split()))

firstValue = max(data)
data.remove(firstValue)
secondValue = max(data)

result = 0
tempCount = 0
for i in range(0, m):
    if tempCount == k:
        result += secondValue
        tempCount = 0
    else:
        result += firstValue
    tempCount += 1

print(result)

