# 이진트리 순회(깊이 우선 탐색)


# v는 노드 번호를 의미
def DFS(v):
    if v > 7:
        return
    else:
        print(v, end=" ")  # 전위 순회
        DFS(v * 2)  # 왼쪽 자식 노드
        # print(v, end=" ")  # 중위 순회
        DFS(v * 2 + 1)  # 오른쪽 자식 노드
        # print(v, end=" ")  # 후위 순회


DFS(1)  # 루트 노드부터 순회
