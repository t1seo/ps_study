# 부분집합 구하기
# 자연수 N이 주어지면 1부터 N까지의 원소를 갖는 집합의 부분 집합 출력


def DFS(v, n):
    ch = [0] * (n + 1)  # 체크 배열

    if v == n + 1:  # 종착점
        for i in range(1, n + 1):
            if ch[i] == 1:
                print(i, end=" ")
            print()
    else:
        ch[v] = 1  # 사용한다
        DFS(v + 1, n)
        ch[v] = 0  # 사용하지 않는다
        DFS(v + 1, n)


DFS(1, 3)

