# https://programmers.co.kr/learn/courses/30/lessons/77485

def solution(rows, columns, queries):
    answer = []
    cnt = 1
    board = [[0 for _ in range(columns)] for i in range(rows)]
    for i in range(rows):
        for j in range(columns):
            board[i][j] = cnt
            cnt += 1
    minboard = []
    for query in queries:
        oldy, oldx = query[0]-1, query[1]-1
        minn = board[oldy][oldx]  # 8
        st = board[oldy+1][oldx]  # 14
        save = board[oldy][oldx]  # 8
        while True:
            if oldy == query[0]-1: # top 
                if oldx == query[3]-1:
                    newy, newx = oldy + 1, oldx
                else:
                    newy, newx = oldy, oldx + 1
            elif oldy == query[2] -1: # bottom 
                if oldx == query[1]-1:
                    newy, newx = oldy - 1, oldx
                else:
                    newy, newx = oldy, oldx - 1
            elif oldx == query[1] - 1: # left
                if oldy == query[0]-1:
                    print('finished')
                    break
                else:
                    newy, newx = oldy -1, oldx
            elif oldx == query[3]-1: # right
                if oldy == query[2]-1:
                    newy, newx = oldy, oldx -1
                else:
                    newy, newx = oldy+1, oldx
            tmp = board[newy][newx]
            board[newy][newx] = save
            save = tmp
            if board[newy][newx] < minn:
                minn = board[newy][newx]
            if newy == query[0]-1 and newx == query[1]-1:
                board[newy][newx] = st
                break
            # print(board[newy][newx])
            oldy, oldx = newy, newx
        minboard.append(minn)
    # print(board)
            
    return minboard