n = int(input())
s = []
for i in range(n):
  start, end = map(int, input().split())
  s.append([start, end])
s = sorted(s, key = lambda x: x[0])  
s = sorted(s, key = lambda x: x[1])

last = 0
count = 0

for i,j in s:
  if i >= last:
    count += 1
    last = j

print(count)