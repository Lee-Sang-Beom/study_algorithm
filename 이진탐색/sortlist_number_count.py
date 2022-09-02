from bisect import bisect_left, bisect_right


n,x = list(map(int,input('n, x 입력 : ').split()))
array = list(map(int, input('배열 입력 : ').split()))

def count(array, left_value, right_value):
    left_index = bisect_left(array,left_value)
    right_index = bisect_right(array,right_value)
    return right_index - left_index

result = count(array,x,x)
print(result)
