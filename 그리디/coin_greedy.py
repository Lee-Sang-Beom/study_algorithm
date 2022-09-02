#거스름돈 1260원 : O(화폐의개수)->O(n)

money = 1260
count = 0

array = [500, 100, 50, 10]

for i in array:
    coin_num = money // i # 총 금액인 money를 큰 값단위부터 나눠 몫을 구함
    count += coin_num # 총 동전 개수 증가
    print(f"{money}원을 {i}원으로 나누어 그리디 알고리즘 적용 -> {coin_num}개")
    money -= coin_num * i

print("총 동전 개수", count)
