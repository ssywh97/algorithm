from collections import deque

N, M, V = map(int, input().split())
graph = [[0]*(N+1) for i in range(N+1)]

for i in range(M):
    a,b = map(int,input().split())
    graph[a][b]=graph[b][a]=1
visit_list = [0] * (N + 1)

def dfs(V):
  visit_list[V] = 1
  print(V, end=' ')
  for i in range(1, N +1):
    if (visit_list[i] == 0 and graph[V][i] == 1):
      dfs(i)

def bfs(V):
  queue = deque([V])
  visit_list[V] = 0
  while queue:
    V = queue.popleft()
    print(V, end=' ')
    for i in range(1, N + 1):
      if(visit_list[i] == 1 and graph[V][i] == 1):
        queue.append(i)
        visit_list[i] = 0
        


dfs(V)
print()
bfs(V)

