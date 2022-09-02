list = [7,5,9,0,3,1,6,2,4,8]

for i in range(len(list)):
    min_index = i
    for j in range(i+1, len(list)):
        if list[min_index] > list[j]:
            min_index = j
    list[i], list[min_index] = list[min_index], list[i] #swap : 현재 i위치값와 제일 작은값이존재하는 min_index를 변경

print(list)
