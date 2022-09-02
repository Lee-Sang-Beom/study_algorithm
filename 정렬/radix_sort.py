list = [7,5,9,0,3,1,6,2,4,8,0,5,2]
count = [0]*(max(list)+1)

for i in range(len(list)):
    count[list[i]]+=1 #list의 각 값을 count의 index로써 변환하여 카운트 증

print(count[0])
for i in range(len(count)): # count 배열을 하나하나 확인하면서
    for j in range(count[i]): # count[i] 숫자가 몇인지 확인
        print(i, end=" ") # count[i]의 숫자만큼 i를 반복출력 
