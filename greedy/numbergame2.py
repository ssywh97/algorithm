# 이중 반복문을 사용하는 풀이

n, m = map(int, input().split())

result = 0

for i in range(n):
    data = list(map(int, input().split()))
    min_vaue = 10001
    
    for a in data:
        min_vaue = min(min_vaue, a)

    result = max(result, min_vaue)

print(result)