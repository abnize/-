# 스택(stack)
# - 쌓아 울리는 형태를 가진 자료구조
# - 후입선출(LIFO, Last In First Out)의 구조를 가짐

# 주요 동작
# - push : 데이터 삽입
# - pop : 데이터 추출
# - peek / top : 가장 위의 데이터 확인
# - isEmpty : 스택이 비어있는지 확인

stack = []

stack.append(10)
stack.append(20)
stack.append(30)
print("현재 스택은 : ", stack)

top = stack.pop()
print("pop된 값 : ", top)
print("pop이 실행된 후 스택 : ", stack)

if stack:
    print("현재 가장 위의 있는 데이터(top)의 값 : ", stack[-1])

if not stack:
    print("스택이 비어있습니다.")
else:
    print("스택에 값이 존재합니다.")

