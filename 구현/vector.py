# 시뮬레이션/완전탐색문제 -> 2차원 공간에서의 방향벡터가 자주 활용

   # 동, 북, 서, 남
dx = [0, -1, 0, 1] #세로(행)
dy = [1, 0, -1, 0] #가로(열)

x,y = 2,2

for i in range(4):
    # 다음위치
    nx = x+dx[i]
    ny = y+dy[i]
    print(nx,ny)

#  (2,3) (1,2) (2,1) (3,2)
