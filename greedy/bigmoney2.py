n, m, k = map(int, input().split())
data = list(map(int, input().split()))

data.sort()
first = data[n - 1]
second = data[n - 2]

count = int(m / (k + 1)) * k
count += m % (k + 1) #만약 m을 k+1로 나누었을때 나머지가 나온다면 그횟수만큼 count에 더해서 최댓값을 더하는 횟수를 늘려줌

result = 0
result += count * first #가장 큰 수 더하기
result += (m - count) * second # 두번째로 큰 수 더하기

print(result)