from collections from deque # bfs는 queue를 사용, dfs는 재귀 또는 스택 사용

def bfs(graph, start, visited):
    queue = deque([start]) # 큐 생성
    visited[start] = True

    while queue:
        v=queue.popleft() # 가장 먼저들어온 거 꺼냄
        print(v, end = " ")
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True
                



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
bfs(graph, 1, visited)
