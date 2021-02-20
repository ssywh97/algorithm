N = int(input())
K = int(input())
arr = list(map(int, input().split()))

if K >= N:
  print(0)
else:
  arr.sort()
  arr2 = []

  for i in range(1, N):
    arr2.append(arr[i] - arr[i - 1])
  arr2.sort() #0, 1, 2, 2, 3

  for i in range(K - 1):
    arr2.pop()

  print(sum(arr2))


