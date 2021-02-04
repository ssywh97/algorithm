from collections import deque

def bfs(graph, start, visited):
    queue = deque([start])
    visited[start] = True
    while queue:
        v = queue.popleft()
        print(v, end=' ')
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True

graph = [
    [], #0번
    [2, 3, 8], #1번 노드
    [1, 7], #2번 노드
    [1, 4, 5], #3번 노드
    [3, 5], #4번 노드
    [3, 4], #5번 노드
    [7], #6번 노드
    [2, 6, 8], #7번 노드
    [1, 7] #8번 노드
]

visited = [False] * 9