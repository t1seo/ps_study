# https://www.acmicpc.net/problem/1915
# 다이나믹 프로그래밍 > 가장 큰 정사각형 

from collections import deque

def make_board(y, x, dp):
	board = []
	for i in range(y):
		board.append(dp[i])
	return (board)

def solution(y, x, dp):
	board = make_board(y, x, dp)
	for i in range(1, y):
		for j in range(1, x):
			if dp[i][j] == 1:
				board[i][j] = min(dp[i-1][j], dp[i-1][j-1], dp[i][j-1])+1
	maxx = 0
	for i in range(y):
		for j in range(x):
			if maxx < board[i][j]:
				maxx = board[i][j]
	print(maxx**2)
	return (maxx**2)

y, x = input().split()
dp = []
for i in range(int(y)):
	tmp = input()
	lst = list(tmp)
	lst2 = []
	for j in range(len(lst)):
		lst2.append(int(lst[j]))
	dp.append(lst2)
solution(int(y), int(x), dp)
# solution(dp)
# solution(4, 4, [[0, 1, 0, 0], [0, 1, 1, 1], [1, 1, 1, 0], [0, 0, 1, 0]])

"""
4 4 
0110 
0000
0000
0000
0

4 4
0100
0111
1110
0010
4

1 1 
1 
1

"""