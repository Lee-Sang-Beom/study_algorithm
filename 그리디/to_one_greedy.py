# 최대한 많이 나누는 것이 point

n,k = map(int, input().split())
result = 0

while True:
    target = (n//k)*k # 나누어 떨어지는 값 탐색
    result += (n-target) # 나누어 떨어지지 못한 횟수 
    n = target

    if(n < k): # k로 나누지 못할정도로 n이 작아지면 탈출
        break
    
    result+=1 # n을 계속해서 나눔
    n //= k # n값을 k로 나눈 몫의 값을 n으로 취

result += n-1 # 마지막으로 남은 수에 대해 1씩 빼기
print(result)


== 
- 혹은 

n,k = list(map(int, input('n,k입력 : ').split()))
result = 0

while n!=1:
    if(n%k==0):
        n = n// k
        result+=1
    else:
        n=n-1
        result+=1
        
print(result)
