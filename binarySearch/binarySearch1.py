###########재귀함수 사용 이진탐색코드###################
def binary_search(array, target, start, end):
  if start > end:
    return None
  mid = (start + end) // 2 #중간값의 인덱스 찾기
  #중간값인덱스의 요소가 target과 같으면 반환
  if array[mid] == target:
    return mid
  #중간점의 값보다 찾고자 하는 값이 작은 경우 왼쪽 확인
  elif array[mid] > target:
    return binary_search(array, target, start, mid - 1)
  else:
    return binary_search(array, target, mid + 1, end)

#n(원소의 개수)의 값과 target값을 입력받음
n, target = list(map(int, input().split()))
#전체 원소 입력받기
array = list(map(int, input().split()))

#이진탐색 수행 결과 출력
result = binary_search(array, target, 0, n - 1)
if result == None:
  print("찾고자 하는 원소가 존재하지 않습니다.")
else:
  print(result + 1)