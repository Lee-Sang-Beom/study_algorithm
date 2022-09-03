import heapq
import sys

INF = int(1e9) # 무한 의미

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
            

# input = sys.stdin.readline()

# 노드 개수, 간선 개수
n,m = map(int, input().split())

# 출발 노드
start = int(input())

# 각 노드에 연결된 노드정보를 담는 리스트 만들기
graph = [[] for i in range(n+1)]

# 최단거리 정보저장 : 처음은 무
distance = [INF]*(n+1)

# 도달할 수 있는 노드의 개수 : 이게 최대인 것이, 가장 멀리 전보가 간다는 뜻
count = 0

# 도달 가능한 노드 중, 가장 멀리있는 노드와 최단거리
max_distance = 0

for _ in range(m):
    a,b,c = map(int, input().split())

    # a번 노드에서 b번 노드로 가는 [비용]이 c
    graph[a].append((b,c))
    
dijkstra(start)

for d in distance:
    if d != INF:
        count+=1 # 전보 가능한 노드개수
        max_distance = max(d, max_distance) # 가장 멀리있는 도시확인 = 비용이 가장 큰 것 (distance배열)
        

print(count-1, max_distance) # 전보하는 도시개수 (전보시작점 제외), 가장 큰 비용 출력
