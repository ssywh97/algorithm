h = int(input())
#n = int(input())
count = 0 #일정 숫자가 들어간 횟수 세는 변수
for i in range(h + 1): #시
    for j in range(60): #분 
        for k in range(60): #초
            if '3' in str(i) + str(j) + str(k):
                count += 1
print(count)