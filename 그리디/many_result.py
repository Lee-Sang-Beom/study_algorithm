# 위치의 값이 0or1이면 덧셈, 나머지는 곱셈으로 

string = list(input("문자열을 입력하세요 : "))
result = 0
i = 0

while i < len(string):
    
    num = int(string[i])
    if num <= 1 or result <= 1:
        result += num
    else:
        result *= num

    i += 1


print(result)
