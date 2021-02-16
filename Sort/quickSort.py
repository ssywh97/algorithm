array = [5, 7, 9, 0, 3, 1, 6, 2, 4, 8]

def quick_sort(array, start, end):
  if start >= end: #원소가 1개인 경우 종
    return
  
  pivot = start #피벗은 첫번째 원소
  left = start + 1 #왼쪽인덱스는 첫번째 다음 원소부터
  right = end #오른쪽 인덱스는 마지막 원소부터
  
  while left <= right: #왼쪽인덱스가 오른쪽 인덱스보다 작거나 같으면
  #피벗보다 큰 데이터를 찾을 때까지 반복
    while left <= end and array[left] <= array[pivot]:
      left += 1 #왼쪽인덱스 하나 증가
    
    while right > start and array[right] >= array[pivot]:
      right -= 1 #오른쪽 인덱스 하나 감소
      #왼쪽인덱스가 오른쪽 인덱스를 엇갈렸다면 
    
    if left > right: 
      #오른쪽 인덱스와 피벗을 교체
      array[right], array[pivot] = array[pivot], array[right]
    
    else: #엇갈리지 않았다면 작은데이터와 큰 데이터를 교체
      array[left], array[right] = array[right], array[left]
  
  #분할과정: start부터 right -1 분할, right+부터 end까지 분할
  quick_sort(array, start, right - 1)
  quick_sort(array, right + 1, end)

quick_sort(array, 0, len(array) - 1)
print(array)