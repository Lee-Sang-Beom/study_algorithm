x=int(input())
d = [0] * 30001 # x=1이면, 자기자신이므로 연산수행할 필요 x. 연산을 사용하는 최솟값

# ai = i를 1로만들기 위한 최소연산횟수.

for i in range(2,x+1):

    # 현재 수에서 1을 빼는경우
    d[i] = d[i-1]+1

    if i%2==0: #2로 나누어진다면
        d[i] = min(d[i], d[i//2]+1)
        # 만약 i가 4일때, d[2]:2를 1로나누기위한 최소연산 횟수에 +1하면됨 (이전결과에 +1하는 것으로)
        # d[i//2]는 이미 구해졌기 때문에 i일때 2로 나누어지는 행위가 1회 연산이고, 그 연산 이후에는 memorization된 값을 추가로 이용하는 것
        
    if i%3==0:
        d[i] = min(d[i], d[i//3]+1)
        
    if i%5==0:
        d[i] = min(d[i], d[i//5]+1)

print(d[x])

