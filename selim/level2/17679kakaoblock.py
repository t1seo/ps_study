# https://programmers.co.kr/learn/courses/30/lessons/17679
# 2018 KAKAO BLIND RECRUITMENT > [1차] 프렌즈4블록

def four_block(i, j, board):
    global boomed
    if board[i][j] != board[i][j+1]:
        return 0
    if board[i][j] != board[i+1][j]:
        return 0
    if board[i][j] != board[i+1][j+1]:
        return 0
    boomed[i][j] = 1
    boomed[i][j+1] = 1
    boomed[i+1][j] = 1
    boomed[i+1][j+1] = 1
    return 1

def solution(m, n, board):
    global boomed
    answer = 0
    for i in range(len(board)):
        board[i] = list(board[i])
    # print(board)
    
    cnt = 0
    while True:
        boomed = [[0 for i in range(n)] for j in range(m)]
            
        for i in range(0, m-1): # 세로
            for j in range(0, n-1): # 가로 
                four_block(i, j, board) # 4블록 
        # print('first', boomed)
        orgcnt = cnt
        cnt = 0
        for i in range(m):
            cnt += sum(boomed[i])
        if (orgcnt == cnt):
            break
        
        for i in range(m-1, -1, -1):
            for j in range(0, n):
                if boomed[i][j] == 1:
                    y = i-1
                    while (y >= 0 and boomed[y][j] == 1):
                        y = y - 1
                    if y == -1:
                        board[i][j] = 0
                    else : 
                        board[i][j] = board[y][j]
                        boomed[y][j] = 1
                        board[y][j] = 0
        # print(board)
        # print(boomed)
                        
        
    return sum(board, []).count(0)