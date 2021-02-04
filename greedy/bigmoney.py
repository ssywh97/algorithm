#단순한 풀이
n, m, k = map(int, input().split()) 
data = list(map(int, input().split())) 

data.sort() #정렬
first = data[n-1] #가장큰수(오름차순으로 정렬 했기 때문)
second = data[n-2]
print(data)
result = 0

while True:
    for i in range (k): #k번 반복함으로써 최대 k번 반복해서 더해야하는제약조건을 지킴
        if m == 0:
            break
        result += first
        m -= 1 #한번 더했으므로 횟수 1회 차감 
    if m == 0:
        break
    result += second #두번째로 큰 값을 한번 더해주고(최댓값을 위해) 다시 for반복문을 실행
    m -= 1

print(result)