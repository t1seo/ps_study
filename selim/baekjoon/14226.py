# https://www.acmicpc.net/problem/14226
# 이모티콘
"""https://it-garden.tistory.com/324"""

from collections import deque 

def solution(s):
	ch = [[-1]*(s+1) for i in range(s+1)]
	que = deque()
	que.append([1, 0])
	ch[1][0] = 0 # 화면에 있는 이모티콘, 클립보드 

	while (que):
		x, y = que.popleft() # 넣은 대로 팝한다 

		if ch[x][x] == -1:
			ch[x][x] = ch[x][y] + 1
			que.append([x, x])
		if x + y <= s and ch[x+y][y] == -1:
			ch[x+y][y] = ch[x][y] + 1
			que.append([x+y, y])
		if x-1 >= 0 and ch[x-1][y] == -1:
			ch[x-1][y] = ch[x][y] + 1
			que.append([x-1, y])
	
	answer = ch[s][1]

	for i in range(1, s):
		if ch[s][i] != -1:
			answer = min(answer, ch[s][i])
	print(answer)



s = int(input())
solution(s)

# solution(2) # 2
# solution(4) # 4
# solution(6) # 5
# solution(18) # 8