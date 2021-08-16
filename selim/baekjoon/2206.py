# https://www.acmicpc.net/problem/2206
# 벽 부수고 이동하기 

import sys
from collections import deque

sign = [[0,1], [0,-1], [1,0], [-1,0]]

def solution(visited, board, n, m):
	que = deque()
	visited[0][0][0] = 1
	que.append([0, 0, 0])
	while (que):
		oldy, oldx, brokenwall = que.popleft()
		if oldy == n-1 and oldx == m-1:
			return (visited[oldy][oldx][brokenwall])
		for i in range(4):
			y = oldy + sign[i][0]
			x = oldx + sign[i][1]
			if y >= n or y < 0 or x >= m or x < 0:
				continue
			if (visited[y][x][brokenwall]):
				continue
			if board[y][x] == 0:
				visited[y][x][brokenwall] = visited[oldy][oldx][brokenwall] + 1
				que.append([y, x, brokenwall])
			elif board[y][x] == 1 and brokenwall == 0:
				visited[y][x][1] = visited[oldy][oldx][0] + 1
				brokenwall = 1
				que.append([y, x, brokenwall])
	return -1


y, x = map(int, input().split())
visited = [[[0 for _ in range(2)] for col in range(x)] for row in range(y)]
# visited = []
board = []
for row in range(y):
	numstr = sys.stdin.readline()
	tmp = []
	for col in range(x):
		tmp.append(int(numstr[col]))
	board.append(tmp)
df = solution(visited, board, y, x)
print(df)

# matrix = []
# for row in range(y):
# 	numstr = sys.stdin.readline()
# 	tmp = []
# 	for col in range(x):
# 		tmp.append([int(numstr[col]), 0])
# 	matrix.append(tmp)
# print(matrix)	

"""
6 4
0100
1110
1000
0000
0111
0000
"""