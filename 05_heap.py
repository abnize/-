# Heap
# - 가장 큰 값 또는 가장 작은 값을 빠르게 꺼내기 위한 자료구조
# - 가장 큰 값 : Mas Heap
# - 가장 작은 값 : Min Heap

# 대표 용도
# - 우선순위 큐
# - 다익스트라(Diikstra) 알고리즘
# - 일정/작업 스케쥴링

# Max Heap 구현
import heapq

heap = []

for n in[7,3,5,1,9]:
    heapq.heappush(heap,-n)

    print("힙 구조 : ", )
    print("가장 큰 값 :",)
    print("힙 구조 :",)