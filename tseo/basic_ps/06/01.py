# 10진수 -> 2진수


def DFS(x):
    if x == 0:
        return
    else:
        DFS(x // 2)
        print(x % 2, end="")  # 거꾸로 출력하기 위해서 DFS 호출 밑으로


DFS(10)  # 1010
