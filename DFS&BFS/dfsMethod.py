#graph : 내가 정의한 그래프, v : 방문한 노드(시작은 1번노드), visited : 방문처리여부가 기록된 리스트(처음에는 false)
def dfs(graph, v, visited): 
    visited[v]  = True
    print(v, end=' ')
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)  

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