# 우선순위 큐 : 우선순위가 가장 높은 데이터를 가장 먼저 삭제하는 자료구조
# 우선순위 큐를 구현하기 위해 힙 사용 가능
# 최소힘 : 값이 낮은데이터부터 꺼냄
# 최대힙 : 값이 높은데이터부터 꺼냄
# 이 힙은 (o(log n))의 시간복잡도 가짐 : 삽입/삭제 둘다

import sys
import heapq

# 오름차순 힙 정렬 : 힙 라이브러리는 기본적으로 우선순위가 낮은 최소힙으로 구현됨
def heapsort(iterable):
    h=[]
    result=[]

# 모든 원소를 차례로 삽입 
    for value in iterable:
        heapq.heappush(h, value) # 특정 h 리스트에 데이터 value를 넣음

    for i in range(len(h)):
        result.append(heapq.heappop(h)) # 특정 h리스트에서 데이터 꺼냄
        # pop할때 우선순위가 낮은것부터 꺼내짐 (기본 라이브러리가 최소힙임)

    return result

result = heapsort([1,3,5,7,9,2,4,6,8,0]) # o(nlogn)
print(result)


# 최대 힙 : 내림차순
def heapsort2(iterable):
    h=[]
    result=[]

# 모든 원소를 차례로 삽입 
    for value in iterable:
        heapq.heappush(h, -value) # h에 데이터를 넣을때 데이터 부호를 변

    for i in range(len(h)):
        result.append(-heapq.heappop(h)) # 특정 h리스트에서 데이터 꺼낼 때 부호를 바꿔서 꺼냄

    return result

result = heapsort2([1,3,5,7,9,2,4,6,8,0]) # o(nlogn)
print(result)
