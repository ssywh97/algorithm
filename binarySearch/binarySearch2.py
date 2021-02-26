#############단순 반복문 사용 이진탐색코드################
def binary_search(array, target, start, end):
  while start <= end:
    mid = (start + end) // 2
    #찾은 경우 중간점 인덱스 반환
    if array[mid] == target:
      return mid
    elif array[mid] > target:
      end = mid - 1
    else:
      start = mid + 1
  return None
#n(원소의 개수)의 값과 target값을 입력받음
n, target = list(map(int, input().split()))
#전체 원소 입력받기
array = list(map(int, input().split()))

result = binary_search(array, target, 0, n - 1)
if result == None:
  print("찾고자 하는 원소가 존재하지 않습니다.")
else:
  print(result + 1)