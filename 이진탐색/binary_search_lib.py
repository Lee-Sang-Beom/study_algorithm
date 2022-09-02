from bisect import bisect_left, bisect_right

# ex) [1,2,4,4,8]
# bisect_left(a,x) : 정렬된 순서를 유지하며, 배열 a에 x를 삽입할 가장 왼쪽 인덱스를 반환

# bisect_right(a,x) : 정렬된 순서를 유지하며, 배열 a에 x를 삽입할 가장 오른쪽 인덱스를 반환
                     

a = [1,2,4,4,8]
x=4

print(bisect_left(a,x))  # ['4' 라는 인덱스가 배열 a의 2,3,4번째 위치(들어갈수있는위치의 제일 왼쪽)에 들어갈수있으며, 가장 왼쪽인 2번째 인덱스 반환]
print(bisect_right(a,x)) # ['4' 라는 인덱스가 배열 a의 2,3,4번째 위치(들어갈수있는위치의 제일 우측)에 들어갈수있으며, 가장 우측인 4번째 인덱스 반환]


# 값이 특정 범위에 속하는 데이터 갯수 구하기

def count_by_range(a, left_value, right_value):
    right_index = bisect_right(a,right_value)
    left_index = bisect_left(a,left_value)

    return right_index-left_index

b=[1,2,3,3,3,3,4,4,8,9]

# 값이 4인 데이터 개수
print(count_by_range(b,4,4))

# [-1,3] 범위에 있는 데이터 개수
print(count_by_range(b,-1,3))
    
