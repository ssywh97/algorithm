N = int(input())
S = list(map(int, input().split()))

count = 0
Max = 0
ans = 0

for i in S:
    if i > Max:
      Max = i
      count = 0
    else:
      count += 1
    ans = max(ans, count)

print(ans)
print(1)