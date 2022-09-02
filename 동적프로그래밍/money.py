n,m = list(map(int,(input('go : ').split()))) # n : 화폐종류, m: 가치
money_list = []
for i in range(n): # 화폐종류 수만큼 반복
    money_list.append(int(input('입력 : ')))

d=[10001]*(m+1) # 초기화 : [10001]이라는 무한값으로. 배열 d는 최소연산회수를 저장

d[0]=0
                      
for i in range(n): # 각 화폐마다 봄
    for j in range(m+1): # 각 화폐마다 보면서 최솟값을 찾아줄거임. 각 화폐단위부터 총 돈까지 반복하며, 최솟값을찾아봄
        if d[j-money_list[i]] != 10001: # 만약 현재 가치(보유 돈)에서 money_list의 값만큼 뻈을때 최소 동전 수 값이 존재하면,
            d[j] = min(d[j], d[j-money_list[i]]+1) # 이전 값이 존재해도, n번만큼 돌면서 이미 입력된 d[j]보다 작지 않을 수 있기에 비교

if d[m]==10001:
    print("결과 못찾음")
else:
    print(d[m])

print(d[0])
