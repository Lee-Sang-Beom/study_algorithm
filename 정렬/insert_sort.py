list = [7,5,9,0,3,1,6,2,4,8]

for i in range(1, len(list)):
    for j in range(i,0,-1): # i번째부터 0번째까지 이동하며, 적절한위치탐색
        if list[j] < list[j-1]: 
            list[j], list[j-1] = list[j-1], list[j]
        else:
            break #처음부터 순차적으로 정렬되므로, 만약 위치가 바꿀게없다면 앞은 이미 정렬이 다 된거니 해당 반복문 탈출
            


print(list)
 
