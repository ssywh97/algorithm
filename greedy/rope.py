N = int(input())
array = []
for _ in range(N):
  array.append(int(input()))

def rope():
  result = 0
  array.sort(reverse=True)
  for i in range(N):
    array[i] = array[i] * (i+1)

  return max(array)

print(rope())