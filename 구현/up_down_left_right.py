# 시작좌표는 (1,1)

x,y=1,1
size = int(input("size 입력 : "))
plans = list(input('계획 입력 : ').split())

# L, R, U, D
dx = [0,0,-1,1] #행
dy = [-1,1,0,0] #열
move_type = ['L','R','U','D']

for plan in plans:
    for i in range(len(move_type)):
        if plan == move_type[i]:
            nx = x+dx[i]
            ny = y+dy[i]

            if nx < 1 or ny < 1 or nx > size or ny > size:
               continue
            
            x,y = nx, ny

print(x,y)
