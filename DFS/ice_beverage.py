n,m=map(int,input().split())
graph=[]

for i in range(n):
    graph.append(list(map(int, input())))

print(graph) # 00110 00011 11111 00000

def dfs(x,y):
    if x <= -1 or x>=n or y<=-1 or y>=m:
        return False

    # 방문하지 않은 노드에 대해.. (0이 서로 연결되었으니)
    if graph[x][y] == 0:

        # 해당 노드를 방문했음을 표시
        graph[x][y] = 1

        # '연결된 다른 0지점은 중복으로 result+=1되면 안되므로"연결된곳으로 이동하여 반복
        dfs(x-1,y)
        dfs(x,y-1)
        dfs(x+1,y)
        dfs(x,y+1)
        return True

    return False
    
# 모든 노드에 대해 음료 채우기
result=0

for i in range(n):
    for j in range(m):
        if dfs(i,j) == True: #I,J의 모든 시점에서 연결된 것을 탐
            result+=1

print(result)
