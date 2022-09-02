from collections import deque

n,m=map(int,input().split())
graph=[]

for i in range(n): #n은 행
    graph.append(list(map(int, input())))

# 상하좌우
dx = [-1,1,0,0]
dy = [0,0,-1,1]

def bfs(x,y):
    queue = deque()
    queue.append((x,y))
    while queue:
        x,y=queue.popleft()

        # 현 위치에서 4방향 위치 확인
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]

            if nx<0 or nx>=n or ny<0 or ny>=m:
                continue

            # 괴물을 만난 경우, 무시
            if graph[nx][ny]==0:
                continue

            # 해당 노드를 처음 방문하는 경우, 최단거리기록
            # 이동한 노드에는 시작점부터 거리를 넣음 
            if graph[nx][ny]==1:
                graph[nx][ny] = graph[x][y] + 1
                queue.append((nx,ny)) #bfs특성상 이미지나온 0,0위치는 큐에서 꺼내졌으니 되돌아갈일 x

    return graph[n-1][m-1] # 가장 오른쪽 아래까지 최단거리반환

print(bfs(0,0)) # 0,0과 n-1,m-1 위치는 항상 1
