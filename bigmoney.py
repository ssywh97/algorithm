n, m, k = map(int, input().split()) 
data = list(map(int, input().split())) 

data.sort() #정렬
first = data[n-1] #가장큰수(오름차순으로 정렬 했기 때문)
second = data[n-2]
print(data)
result = 0

while True:
    for i in range (k):
        if m == 0:
            break
        result += first
        m -= 1 #한번 더했으므로 횟수 1회 차감 
    if m == 0:
        break
    result += second
    m -= 1

print(result)