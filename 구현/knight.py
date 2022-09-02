row=int(input('행 좌표 입력(1~8) : '))
input_data = input('열 좌표 입력(문자a~h) : ')
column=int(ord(input_data))-int(ord('a'))+1

steps=[(-2,-1), (-1,-2), (1,-2), (2,-1), (2,1), (1,2), (-1,2), (-2,-1)]

result=0
for step in steps:
    next_row=row+step[0]
    next_column = column+step[1]

    if(next_row>=1 and next_row <=8 and next_column>=1 and next_column<=8):
       result+=1

print(result)
