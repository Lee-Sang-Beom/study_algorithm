def dfs(graph, v, visited):
    visited[v] = True
    print(v, end=' - ')

    for i in graph[v]:# 깊은거부터 꺼냄
        if not visited[i]:
            dfs(graph, i, visited)


# 각 노드가 연결된 정보를 표현(2차원리스트)
graph = [
    [], # 0번째는 없으니 생략
    [2,3,8], # 1번노드는 2,3,8과 연
    [1,7],
    [1,4,5],
    [3,5],
    [3,4],
    [7],
    [2,6,8],
    [1,7]
]

visited = [False]*9 # 각 노드의 방문정보 표현(1차원 리스트)
dfs(graph, 1, visited)
