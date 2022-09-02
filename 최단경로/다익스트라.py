# O(n**2)임.
# 노드 개수가 10000개가 넘어가면 큰일

import sys
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

    # a번 노드에서 b번 노드로 가는 비용이 c. 근데 [b,c]로 해야할거같음
    graph[a].append((b,c))

# 방문하지 않은 노드 중, 최단거리가 가장 짧은 노드의 번호 반환
def get_smallest_node():

    #처음은 무한
    min_value = INF
    index=0
    for i in range(1, n+1):
        # 1번부터 n번까지의 노드 중, 방문하지 않았고 거리값이 가장 작은 노드번호 반
        if distance[i] < min_value and not visited[i]:
            min_value = distance[i]
            index=i
    return index

def dijkstra(start):

    # 출발노드 초기화, 방문처리
    distance[start]=0
    visited[start]=True

    # 출발노드로 부터 당장 도달가능한 노드까지의 거리 계산 후 갱신
    for j in graph[start]:
        distance[j[0]] = j[1] # start 노드에서 각 j[0]번 노드로 가는데 걸리는 비용이 j[1]에 저장됨 

    # 총 n-1개 (start)노드에 대해
    for i in range(n-1):

        # 매번 짧은 노드 선택하고 방문처리
        now = get_smallest_node()
        visited[now] = True

        # 제일 짧은거리의 노드에 대해
        for j in graph[now]:

            # 현재 now위치까지 거리정보가 저장된 것 + j[1]은 j[0]으로이동하기 위한 비용 = 더하면 now->j[0]으로 가는 비용의 총합이 계산됨 
            cost = distance[now]+j[1]
            if cost<distance[j[0]]: # 이게 기존의 테이블에 저장된 값보다 우수하면 갱신
                # j[0] : 이동하려는 노드정보
                # distance[a] : a까지 최소경로
                # distance[j[0]]: 이동하려는 노드까지의 최소경
                distance[j[0]]=cost


dijkstra(start)

for i in range(1, n+1):
    if distance[i]==INF:
        print('infinity')
    else: # 각 i번노드까지 가는 최소경로가 출력
        print(distance[i])
