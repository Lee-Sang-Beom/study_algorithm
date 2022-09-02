# 절단기 높이 0~10억 탐색범위를 보면 반드시 이진탐색 떠올려야함 
# 현재 이 높이로 자르면 조건을 만족하는가를 확인하면서 중간점과 시작점을 높여감
# 조건만족시 결과저장, 조건불만족시 결과미저장 -> 조건불만족시, 중간점 내림
# 이진탐색을 더 수행할 수 없을때 저장된 결과가 최적값
# 중간점 값은 시간이 지날수록 최적값이 되므로, 과정 반복하면서 얻을수있는 떡 길이 합이 필요 떡 길이보다 크거나 같을때마다 중간값 기

# 떡 개수와 요청 떡 길이 입력
n,m=list(map(int,input('n,m 입력: ').split()))

# m_height : 각 떡의 개별높이 기록 ex)19 14 10 17
array =list(map(int,input('떡 높이 입력: ').split()))

# 이진탐색 수행
result= 0

start=0
end=max(array)

while(start<=end):
    total = 0
    mid=(start+end)//2
    for x in array:
        # 떡 하나하나를 잘랐을 때 떡의 길이 계산
        if x > mid:
            total = total + (x-mid)

    # total된 떡의 양이 부족하면 더 많이 자름 (왼쪽 부분 탐색)
    if total < m:
        # 부족할 경우 결과를 저장하지 않음
        end= mid-1 # 더 많은 떡을 잘라내기 위해 절단기준 길이를 좀 낮춰봄. 그를 위해 끝점을 낮춰봄 (mid는 직접 결정하지 x)

    # total된 떡 양이 많으면, 너무 over되었으니, 시작점을 중간점의 오른쪽으로 옮김
    # 중간점(절단점) mid기준 남는 떡의 길이가 over이니 start는 mid보단 커야함
    else:
        result = mid # 현재 중간점 기록을 저장
        start = mid+1

print(result)

# 어렵다 : https://www.youtube.com/watch?v=94RC-DsGMLo&list=PLRx0vPvlEmdAghTr5mXQxGpHjWqSz0dgC&index=5
