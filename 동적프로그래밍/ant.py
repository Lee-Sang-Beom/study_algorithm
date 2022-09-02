n = int(input('식량창고 개수 : ')) #4
k = list(map(int, input('식량 개수를 각각 입력 : ').split())) #1 3 1 5

# 2가지경우: i-1번째 위치를 턴 경우와 i-2번째 위치를 턴 경우
# ai=i번째 식량까지의 최적해 (식량최대값)
# ki=1번째 식량창고에있는 식량 양
# ai = max(ai-1, ai-2+ki)

# 앞선 결과 저장
d=[0]*100

# bottom-up
d[0]=k[0]
d[1]=max(k[0],k[1]) # 더 큰거 선택 : i번째로 갈수록 최대값인걸 고르는게 문제니까

for i in range(2, n):
    d[i] = max(d[i-1], d[i-2]+k[i]) # 항 칸 이상 떨어진 식량창고는 항상 털수있어서, a[i-2]이하에 추가 조건식을 달 필요는 없음!)

print(d[n-1]) # 최종 i번째 값
