#배열 원소의 갯수 n, 변경가능횟수 k 입력받기
n, k = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

a.sort() #오름차순 정렬
b.sort(reverse = True) #내림차순 정렬

#k의 값만큼 반복하면서 비교 후 swap
for i in range(k):
  if a[i] < b[i]:
    a[i], b[i] = b[i], a[i]
  else:
    break

#원소의 합 출력
print(sum(a))