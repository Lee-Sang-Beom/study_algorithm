# 1번 회사에서 k번 회사 방문 후, x번 회사로 이동 (이것의 최소시간은?)
# arr[1,k] + arr[k,x]가 최소인 값을 구해야..!

INF = int(1e9) # 무한을 의미하는 10억

# 노드 개수와 간선의 개수 입력받기
n=int(input())
m=int(input())

# 2차원 리스트(그래프 표현)을 만들고, 무한으로 초기화
# n+1은 각 노드가 1번부터 출발함을 가정 (0번을 버리기)
graph = [[INF] * (n+1) for _ in (n+1)]

# graph[i][i]는 0으로 만드는 작업
for a in range(1,n+1):
    for b in range(1,n+1):
        if a==b:
            graph[a][b]=0


# 각 간선에 대한 정보를 입력받음. 여기서 graph[a][b]=[b][a]
for _ in range(m):
    # a->b로 가는 비용 1
    a, b = map(int, input().split())
    graoh[a][b]=1
    graoh[b][a]=1

k,x = map(int, input("거쳐갈노드 k, 목적지 노드 x 입력 : ").aplit())

# 점화식에 따라 플로이드 위셜 알고리즘 수행
for k in range(1, n+1):
    for a in range(1, n+1):
        for b in range(1, n+1):
            graph[a][b] = min(graph[a][b], graph[a][k]+graph[k][b])

# 최소거리출력 1>k>x : 그래프의 [1][k]+[k][x]를 더하면됨
distance = graph[1][k]+graph[k][x]
print(distance)
