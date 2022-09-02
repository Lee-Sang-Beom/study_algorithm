def factorical_iterative(n):
    result = 1
    for i in range(n+1):
        if(i==0):
            continue
        result*=i

    return result

def factorial_recursive(n):
    if n<=1:
        return 1

    return n * factorial_recursive(n-1)

print(factorical_iterative(5)) # 반복구현
print(factorial_recursive(5)) # 재귀구현
