import sys
from collections import deque

# 2 <= N <= 100 보드의 크기에 맞춰 미리 전역변수로 만들어 놓기 
board = [[0 for col in range(102)] for row in range(102)]

# 확인을 위한 함수 board 크기만큼 프린트 
def print_board(n):
	for i in range(1, n + 1):
		for j in range(1, n + 1):
			print(board[i][j], end = '')
		print()

# 풀이함수
def solution(n, apples, k, moves):
	for i in range(len(apples)): #apple을 보드에 1로 설정 
		y = apples[i][0]
		x = apples[i][1]
		board[y][x] = 1
	sec = 1						# 시간(초)
	y, x = 1, 1					# 현재 y, x 좌표
	board[1][1] = 2				# 시발점
	mov = 0						# moves의 인덱스
	signs = [[0,1],[1,0],[0,-1], [-1,0]] # 방향따른 y, x좌표 더하기 빼기 
	vec = 0						# 방향 전환 인덱스
	body = deque([[1,1]])		# 뱀의 몸 좌표 저장 
								# 머리는 항상 append로, 꼬리는 popleft로 제거 

	while (1):
		y = y + signs[vec][0] 	#y, x 좌표 이동 
		x = x + signs[vec][1]
		if (y > n or x > n or y < 1 or x < 1): 
			# print('out of range') 	# 보드를 벗어나면 out of range
			print(sec)
			return 
		if (board[y][x] == 2):
			# print('already body')		# 몸이 겹치면 already body 
			print(sec)
			return 
		
		if board[y][x] != 1 : # 만약 apple이 아니면 꼬리는 잘라주어야 하므로 
			tmp = body.popleft()				# popleft로 마지막 꼬리 잘라주고 
			board[int(tmp[0])][int(tmp[1])] = 0 # 0 빈공간으로 초기화
		body.append([y, x])
		board[y][x] = 2

		if (mov < k and moves[mov][0] == sec): # 방향 전환하기
			if (moves[mov][1] == 'D'):			# 만약 'D'면 오른쪽 
				vec += 1
			else:					# 아니면 왼쪽 돌기 
				vec -= 1
			# print(sec, signs[mov])
			vec %= 4
			mov += 1
		sec += 1

n = int(sys.stdin.readline())
k = int(sys.stdin.readline())
apples, moves = [], []
for i in range(k):
	a, b = map(int, sys.stdin.readline().split())
	apples.append([a, b])

k = int(sys.stdin.readline())
for j in range(k):
	a, b = sys.stdin.readline().split()
	moves.append([int(a), b])

solution(n, apples, k, moves)

# solution(6, [[3, 4], [2, 5], [5, 3]], [[3, 'D'], [15, 'L'], [17, 'D']])