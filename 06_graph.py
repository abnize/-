# graph
# - 정점(Vertex)과 간선(Edge)로 구성되어 여러 노드간의 관계를 표현하는 자료구조
# from symtable import Class

# 특징
# - 비선형구조 : 데이터를 일렬로 정렬하지 않고 복잡한 연결 관계를 가짐
# - 사이클 : 트리와 달리 정점간의 순환(사이클)이 가능
# - 다양한관계 표현 : 부모 - 자식처럼 계층적인 관계뿐만이 아니라  복잡하게 얽힌 연결 관계를 표현할 수 있음.

# 종류
# - 무방향 그래프 : 방향이 없어서 양방향 이동이 가능
# - 방향 그래프 : 한쪽 방향을 가져서 한쪽으로만 이동이 가능
# - 가중치 그래프 : 각 간선별로 가중치 또는 비용이 할당된 그래프
# - 완전 그래프 : 모든 방향으로 이동이 가능한, 최대치의 간선을 가진 그래프

# 무방향 그래프 구현
graph = {
    1: [2,3],
    2: [1,4],
    3: [1,4],
    4: [2,3]
}

def bfs (start):
    visited = [] # 방문 기록을 저장할 리스트
    queue = [start] # 방문할 데이터의 후보

    while queue:
        # queue의 가장 앞에 있는 요소 제거 후 제거한 요소를 반환
        node = queue.pop(0)

        if node not in visited: # 현재 node 값이 방문 기록(visited)에 없다면
            visited.append(node)
            queue.extend(graph[node])
        print(visited)

    bfs(1)

