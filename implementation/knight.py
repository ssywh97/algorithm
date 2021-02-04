input_data = input()  #ex) a2 : input_data[0] = a, input_data[1] = 2
row = int(input_data[1])
column = int(ord(input_data[0])) - int(ord('a')) + 1

steps = [(-2, -1), (-1, -2), (1, -2), (2, -1), (2, 1), (1, 2), (-1, 2), (-2, 1)]

result = 0
for step in steps:
    next_row = row + step[0] #(-2, -1) 에서 step[0]은 -2, step[1]은 -1
    next_column = column + step[1]
    if next_row >=1 and next_row <= 8 and next_column >= 1 and next_column <= 8:
        result += 1

print(result)