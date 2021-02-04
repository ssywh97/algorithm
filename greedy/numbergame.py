# min()함수를 활용하는 방법
# 입력예시 : 3 3 
#           3 1 2
#           4 1 4
#           2 2 2 
# 출력예시 : 2

n, m = map(int, input().split())

result = 0 #결과값 변수

for i in range(n): #행의 갯수만큼 반복
    data = list(map(int, input().split()))
    min_value = min(data) #리스트의 값중 최솟값을 저장
    result = max(result, min_value) #result 와 min_value중에 큰 값을 result에 저장

print(result)