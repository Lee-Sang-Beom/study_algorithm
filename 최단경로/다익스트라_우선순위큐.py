import heapq

input = sys.stdin.readline()
INF = int(1e9) # 무한 의미

# 노드 개수, 간선 개수
n,m = map(int, input().split())

# 출발 노드
start = int(input())

# 각 노드에 연결된 노드정보를 담는 리스트 만들기
graph = [[] for i in range(n+1)]

# 방문 여부 저장 : 처음은 모든 노드 방문x
visited = [False]*(n+1)

# 최단거리 정보저장 : 처음은 무
distance = [INF]*(n+1)

for _ in range(m):
    a,b,c = map(int, input().split())

    # a번 노드에서 b번 노드로 가는 비용이 c
    graph[a].append((b,c))

def dijkstra(start):

    q = []

    # (최소거리, 목표노드) : start로 가기위한 최단경로 0으로 설정하여 우선순위큐 초기화
    heapq.heappush(q, (0,start))
    
    # 출발노드 초기화, 방문처리는 아직 하면안됨
    distance[start]=0

    # 출발노드로 부터 당장 도달가능한 노드까지의 거리 계산 후 갱신
    for j in graph[start]:
        distance[j[0]] = j[1] # start 노드에서 각 j[0]번 노드로 가는데 걸리는 비용이 j[1]에 저장됨 

    while q: #큐가 있는동안
         # q에서 최소거리, 현재노드 뽑아옴
         # 최소 힙이기 때문에, dist가 가장 작은 요소가 뽑혀옴
        dist, now = heapq.heapop(q)

        if distance[now] < dist: # 기존 최소거리가 뽑아온거보다 작으면 === 현재노드가 이미 처리된 적이 있는 노드면
            continue # 항상 최소힙은 오름차순으로 뽑기때문에, distance[now]<dist인 경우는 같은노드인데 최적값이 이미 뽑힌경우로 간주할수있다고 

        for i in graph[now]: # 현재노드와 인접한 다른노드를 뽑아 올거임 
            cost = dist+i[1] # now까지 가기위한 거리 + now위치에서 i[0]노드까지 가기위한 거리
            if distance[i[0]] > cost: # 만약 기존 i[0]까지 가는 최소거리가 now를 거쳐가는게 더 이득이라면
                distance[i[0]] = cost

                # 갱신된 값이 있을때만 큐에 넣어줌 : 그래야 거리가 가장 짧은걸 다음 노드로 선정해서 계속해서 값을 갱신해나갈수있기때문에..!
                heapq.heappush(q, (cost, i[0])) 
            
dijkstra(start)

for i in range(1, n+1):
    if distance[i]==INF:
        print('infinity')
    else: # 각 i번노드까지 가는 최소경로가 출력
        print(distance[i])
