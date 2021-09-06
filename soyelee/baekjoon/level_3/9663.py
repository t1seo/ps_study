def checker(n):
    for i in range(n):
        if board[n] == board[i] or abs(board[n] - board[i]) == n - i:
            return 0
    return 1


def dfs(n):
    global result
    if n >= N:
        result += 1
    else:
        for i in range(N):
            board[n] = i
            if checker(n):
                dfs(n + 1)


N = int(input())
board = [0] * N
result = 0
dfs(0)
print(result)

# board = queen's number for each row

# board[n] == board[i]
# Check column

# abs(board[n] - board[i]) == n - i
# board[n] - n == board[i] - i or board[n] + n == board[i] +i
# Check diagonal

# https://ralp0217.tistory.com/entry/Python3-%EC%99%80-PyPy3-%EC%B0%A8%EC%9D%B4
# Speed : Python > PyPy3
# PyPy3 : JIT - Just in time Compile
