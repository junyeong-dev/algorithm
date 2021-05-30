# 정수 x가 주어질 때 정수 x에 사용할 수 있는 연산은 다음과 같이 4가지이다.
# a. x가 5로 나누어떨어지면, 5로 나눈다.
# b. x가 3로 나누어떨어지면, 3로 나눈다.
# c. x가 2로 나누어떨어지면, 2로 나눈다.
# d. x에서 1을 뺀다
# 정수 x가 주어졌을때, 연산 4개를 적절히 사용해서 1을 만들려고 한다.
# 연산을 사용하는 횟수의 최솟값을 출력하시오.

x = int(input())

target = 1
count = 0
while True:
    if target == x:
        break
    if target * 5 <= x:
        target *= 5
        count += 1
        continue
    elif target * 3 <= x:
        target *= 3
        count += 1
        continue
    elif target * 2 <= x:
        target *= 2
        count += 1
        continue
    else:
        target += 1
        count += 1

print(count)