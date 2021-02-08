array = [140, 97, 29, 231, 77, 58, 7, 399, 197, 200]

for i in range(len(array)):
  min_index = i #일단 처음 원소를 min_index로 지정해놓음
  for j in range(i + 1, len(array)): #처음 원소 다음번부터 루프를 돌면서
    if array[min_index] > array[j]: #min_index로 지정된 처음 원소보다 작은값이 나타나면
      min_index = j #나타난 원소를 min_index로 지정함(스왑x, 최솟값을 찾아나가는 과정)
  array[i], array[min_index] = array[min_index], array[i] #루프를 다 돌아서 최솟값을 찾아냈으면 첫번째 원소와 최솟값의 자리를 바꿔줌
  #과정반복하면서 정렬

print(array)