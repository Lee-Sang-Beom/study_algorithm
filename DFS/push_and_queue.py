# push는 .append(num), .pop()으로 수행
# queue는 deque lib이용

from collections import deque

queue = deque()

queue.append(5)
queue.append(2)
queue.append(3)
queue.append(7)
queue.popleft()
queue.append(1)
queue.append(4)
queue.popleft()

print(queue) # 먼저 들어온 순서대로
queue.reverse()
print(queue)

