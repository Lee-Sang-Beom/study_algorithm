def binary_search(array ,target, start, end): #배열, 찾을 데이터, 시작점, 끝
    if start>end:
        return None
    
    mid = (start+end)//2

    if array[mid]>target:
        return binary_search(array,target,start,mid-1)
    elif array[mid]<target:
        return binary_search(array,target,mid+1,end)
    else:
        return mid
    

n, target = list(map(int, input('원소 수, 찾을 값: ').split()))
array=list(map(int, input('배열 입력 : ').split()))
result=binary_search(array,target,0,n-1)
print(f"{target}은 배열의 {result+1} 번째 위치에있습니다.")
