# 큐 (Queue)
# - 스택과 반대로 아래가 뻥 뚫린 형태를 가진 자료구조
# - 선입선출(FIFO, First In First Out)의 구조를 가짐

# 주요 동작
# - enqueue(data) : 데이터 삽입
# - dequeue() : 데이터 추출
# - front() : 첫번째 요소 확인
# - rear() : 마지막 요소 확인
# - isEmpty() : 비어있는지 확인

from collections import deque

queue = deque()

queue.append("A")
queue.append("B")
queue.append("C")
print("현재 큐: ", queue)

front = queue.popleft()
print("dequeue 된 값 : ", front)
print("dequeue 후 큐 : ", queue)

if queue:
    print("front(맨 앞 요소) : ", queue[0])
    print("rear(맨 뒤) : ", queue[-1])


# 덱 (Deque, Double Ended Queue)
# - 스택과 큐처럼 사용이 가능하며 양쪽에서 삽입/삭제가 가능한 자료구조
dq = deque([2, 4, 6])
print("초기 덱 : ". dq)

dq.append(8) # 오른쪽으로 데이터 삽입
dq.appendleft(0) # 왼쪽으로 데이터 삽입
print("추가 후 덱 : ", dq)

right = dq.pop() # 오른쪽 데이터 삭제
left = dq.popleft() # 왼쪽 데이터 삭제
print("삭제된 값 : ", left, right)
print("삭제 후 덱 : ", dq)