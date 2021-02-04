n = int(input()) #행렬의 크기
x, y = 1, 1 #시작점은 1,1
plans = input().split() #방향계획

#왼오위아래
dx = [0, 0, -1, 1]  #행
dy = [-1, 1, 0, 0]  #렬
move_types = ['L', 'R', 'U', 'D']

#이동 계획을 하나씩 확인
for plan in plans:
    for i in range(len(move_types)): #move_types의 길이만큼 반복
        if plan == move_types[i]:
            nx = x + dx[i]
            ny = x + dy[i]
    #공간을 벗어나는 경우 무시
    if nx < 1 or ny < 1 or x > n or ny > n:
        continue

    x, y = nx, ny
print(x, y)
