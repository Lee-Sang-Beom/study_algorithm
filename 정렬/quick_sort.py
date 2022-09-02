list = [7,5,9,0,3,1,6,2,4,8]

def quick_sort(list ,start, end):
    if start>=end:
        return

    pivot = start
    left = start + 1
    right = end

    while (left<=right):
        while (left<= end and list[left]<=list[pivot]):
            left +=1 
        while (right > start and list[right]>=list[pivot]):
            right-=1
        if (left>right):
            list[right], list[pivot] = list[pivot], list[right]
        else: # 엇갈리지 않은경우는 아직 두 포인터가 교차되지 않음을 의미
            list[right], list[left] = list[left], list[right]

    quick_sort(list, start,right-1) #피봇과 right값이 바뀌었으니, 왼쪽은 right-1이 마지노선
    quick_sort(list,right+1, end)

def quick_sort2(list):
    if len(list)<=1:
        return list

    pivot=list[0]
    tail=list[1:] # 피봇제외 리스트

    left_side = [x for x in tail if x<= pivot] # 분할된 왼쪽부분
    right_side = [x for x in tail if x> pivot]

    # 분할 후 좌측 부분 + 현재 피봇결과가 포함된 리스트 부분 + 오른쪽 부분리스트를 모두 붙임
    return quick_sort2(left_side) + [pivot] + quick_sort2(right_side)


quick_sort(list,0,len(list)-1)
print(list)

print(quick_sort2(list))
 
