#트리(Tree)
# - 계층적 구조를 표현하는 자료구조

# 용어
# - Node : 각각의 데이터
# - Root : 트리의 최상위 노드
# - Child : 부모로부터 연결된 하위 노드
# - Leaf : 더이상 자식이 없는 노드(맨 끝에 위치한 노드)
# - Edge : 노드간의 연결 선
# - Depth : 루트로부터의 거리
# - Height : 트리 전체의 깊이

class Node:
    def __init__(self, value):
        self.value = value # 현재 노드의 값
        self.left = None # 왼쪽 자식
        self.right = None # 오른쪽 자식

# 트리 구성
root = Node(10)
root.left = Node(5)
root.right = Node(15)
root.left.left = Node(2)
root.left.right = Node(7)

# 트리 순회 - 중위 순회(in-order)
def inorder(node):
    if node is None:
        return
    inorder(node.left)
    print(node.value)
    inorder(node.right)