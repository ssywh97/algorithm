# min()함수를 활용하는 방법
# 입력예시 : 3 3 
#           3 1 2
#           4 1 4
#           2 2 2 
# 출력예시 : 2

n, m = map(int, input().split())

result = 0

for i in range(n):
    data = list(map(int, input().split()))
    min_value = min(data)
    result = max(result, min_value)

print(result)