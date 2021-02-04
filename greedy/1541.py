#백준 1541 괄호 문제

numList = list(input().split('-'))  #수식 입력
count = 0
total = 0
print(numList)
for num in numList:
    tmpList = list(map(int, num.split('+')))  #+부호로 스플릿해서 tmplist에 리스트형식으로 넣어줌

    if count == 0: #첫번째 리스트의 값들만 더해서 total에 넣어주고
        count += 1
        total = sum(tmpList)
    else:          #두번째 리스트(count가 0이 아닌 리스트)부터는 리스트의 값을 더해서 total에서 빼줌
        total -= sum(tmpList)

print(total)