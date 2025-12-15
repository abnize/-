# 1. 선택 정렬
# - 가장 작은 값을 골라서 맨 앞으로 보내는 정렬 방식
# - 최소값을 선택한 뒤 그 값을 앞쪽 자리와 교환
def selection_sort(arr):
    for i in range(len(arr)):
        n = len(arr) # 매개변수로 받은 배열의 길이

        for j in range(n-1):
            min_index = i

            for j in range(i+1,n):
                if arr[j] < arr[min_index]:
                    min_index = j

            arr[i], arr[min_index] = arr[min_index], arr[i]
            print(arr)

selection_sort([3, 4, 2, 1, 5])

# 2. 버블 정렬
# - 서로 이웃한 두 요소를 비교하여 큰 수의 자리를 바꾸는 정렬 방식
# - 이 과정을 끝까지 반복하여 가장 큰 값이 거품처럼 맨 위로 올라감
def bubble_sort(arr):
    n = len(arr)

    for i in range(n-1):
        for j in range(n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

    print(arr)

bubble_sort([5, 3, 8, 4, 2])

# 3. 삽입 정렬
# - 왼쪽부터 읽어가며 현재 값을 알맞은 위치에 삽입하는 정렬 방식
def insertion_sort(arr):
    n = len(arr)

    for i in range(1, n):
        key = arr[i]
        j = i-1

        while j >= 0 and key < arr[j] > key:
            arr[j+1] = arr[j]
            j -= 1

        arr[j+1] = key
    print(arr)

insertion_sort([5, 3, 8, 4, 2])

# 4. 셸 장랼
# - 일정 간격(gap)으로 나누어 정렬 후 간격을 줄여가며 정렬하는 방식

# 동작 방식
# - 리스트를 2로 나눈 값(gap)
# - gap만큼 떨어진 요소들끼리 비교 후 교환을 진행
# - gap이 1이 되면 남은 요소들기리를 비교 후 정렬
def shell_sort(arr):
    n = len(arr)

    # 초기 간격(gap)
    gap = n//2

    while gap > 0:
        for i in range(gap, len(arr)): # 초기 간격을 기준으로 요소 교환
            key = arr[i]
            j = i

            while j >= gap and arr[j-gap] > key:
                arr[j] = arr[j-gap]
                j -= gap

            arr[j] = key
        gap //= 2
    return arr

data = [5, 3, 8, 4, 2]
print(shell_sort(data))