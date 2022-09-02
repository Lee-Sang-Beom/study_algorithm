data = input()
result=[]
value=0

for x in data:
    if x.isalpha():
        result.append(x)
    else:
        value += int(x)

sorted(result)
if(value!=0):
    result.append(str(value)) # 현재 리스트상태임. 나중에 string으로 다붙여줘야

print("".join(result)) #리스트->문자열 하는 방법
