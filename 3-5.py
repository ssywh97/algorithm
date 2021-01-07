#1이 될 때까지
n,k = map(int, input().split())

result = 0 #총 연산을 수행하는 횟수

while True:
    target = (n // k ) * k #ex) n = 25, k = 3이면 target은 24
    result += (n - target)
    n = target

    if n < k:
        break
    result += 1
    n //= k

result += (n - 1)
print(result)