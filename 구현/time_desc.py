n = int(input('정수 n입력'))
count=0

for i in range(n+1):
    for j in range(60):
        for k in range(60):          
            string=str(i)+str(j)+str(k)
            if '3' in string:
                count+=1


print(count)
