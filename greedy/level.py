import sys
input=sys.stdin.readline

n = int(input())
level = [int(input()) for _ in range(n)]
cnt = 0
for i in range(n - 1, 0, -1):
  if level[i] <= level[i - 1]:
    cnt += (level[i - 1] - level[i] + 1)
    level[i - 1] = level[i]-1

print(cnt)