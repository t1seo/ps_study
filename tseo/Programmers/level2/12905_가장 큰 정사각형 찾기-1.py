board_1 = [[0, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1], [0, 0, 1, 0]]
board_2 = [[0, 0, 1, 1], [1, 1, 1, 1]]


def solution(board):
    for i in range(1, len(board)):  # num of rows
        for j in range(1, len(board[0])):  # num of columns
            if board[i][j] >= 1:  # 0이 아닌 값들만 업데이트
                # 위, 왼, 좌상단에 인접한 1이 있으면 그 값에 + 1
                board[i][j] = (
                    min(board[i - 1][j], board[i][j - 1], board[i - 1][j - 1]) + 1
                )

    # print(board)
    return max([num for row in board for num in row]) ** 2


print(solution(board_1))
print(solution(board_2))
