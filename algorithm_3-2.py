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

# 위의 알고리즘으로는 10,000이하의 수는 계산 가능 하지만 수가 많아지만 시간 초과의 가능성이 있다
# 그러므로 가장 먼저 반복되는 수열에 대해 파악해야 한다
# 가장 큰 수와 두번째로 큰 수가 더해지는 특정한 수열 형태로 일정하게 반복되기 때문에
# 위의 예시에서는 {6, 6, 6, 5}가 반복된다
# 반복되는 수열의 길이는 k + 1
# 따라서 m을 (k + 1)로 나눈 몫이 수열이 반복되는 횟수가 된다
# 여기에 k를 곱해주면 가장 큰 수가 등장하는 횟수가 된다
# 이때 m이 (k + 1)로 나누어떨어지지 않은 경우도 생각해야 한다 - m % (k + 1)
##### 답안 예시
# n, m, k를 공백으로 구분하여 입력받기
n, m, k = map(int, input().split())
# n개의 수를 공백으로 구분하여 입력받기
data = list(map(int, input().split()))

data.sort()
firstValue = data[n - 1]
secondValue = data[n - 2]

# 가장 큰 수가 더해지는 횟수
count = int(m / (k + 1)) * k
count += m % (k + 1)

result = 0
result += count * firstValue
result += (m - count) * secondValue

print(result)