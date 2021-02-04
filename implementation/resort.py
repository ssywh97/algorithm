data = input() 
result = []
value = 0

for x in data:
    if x.isalpha(): #알파벳이면
        result.append(x) #result에 x값 추가
    else:
        value += int(x)

result.sort()

if value != 0:
    result.append(str(value))

print(''.join(result))
