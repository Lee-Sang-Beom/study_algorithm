#시간복잡도 o(n**3)

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

# 각 간선에 대한 정보를 입력받음. 그리고 그 값으로 초기화
for _ in range(m):
    # a->b로 가는 비용 c
    a, b, c = map(int, input().split())
    graoh[a][b]=c

# 점화식에 따라 플로이드 위셜 알고리즘 수행
for k in range(1, n+1):
    for a in range(1, n+1):
        for b in range(1, n+1):
            graph[a][b] = min(graph[a][b], graph[a][k]+graph[k][b])

# 수행된 결과 출력
for k in range(1, n+1):
    for a in range(1, n+1):
        if graph[a][b]==INF:
            print(f"{a}->{b} 도달 불가")
        else:
            print(graph[a][b], end="")
    print()

