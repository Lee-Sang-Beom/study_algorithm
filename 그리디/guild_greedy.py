# 오름차순 정렬으로 공포도확인 후, 그룹원 추

n = int(input('모험가의 수 : '))
data = sorted(list(map(int, input('공포도 부여 : ').split())))
print(n, fear)

result = 0 # 총 그룹 수
count =0 # 현재 그룹에 포함된 모험가 수

for i in data: # 공포도를 낮은 순으로 확인
    count += 1 # 현 그룹에 모험가 포함
    if count >= i:
        result += 1 # 총 그룹 수 증가
        count = 0  # count를 초기화하여, 공포도에 따른 모험가의 수를 다시 
