# https://www.acmicpc.net/problem/7569
# timeout T.T

from collections import deque 

def check_out(a, b, c, z, y, x):
	if 0 > a or a >= z:
		return False
	if 0 > b or b >= y: 
		return False
	if 0 > c or c >= x : 
		return False
	return True

sign = [[1, 0, 0], [-1, 0, 0], [0, 1, 0], [0,-1,0], [0,0,1], [0,0,-1]]

que = deque()
x, y, z = map(int, input().split())
boxes = [[[0 for i in range(x)] for row in range(y)] for iz in range(z)]
cntminus = 0
for sz in range(z):
	for sy in range(y):
		line = list(map(int, input().split()))
		for i in range(len(line)):
			boxes[sz][sy][i] = line[i]
		for i in range(x):
			if boxes[sz][sy][i] == 1:
				que.append((sz, sy, i, 0))
			if boxes[sz][sy][i] == -1:
				cntminus += 1
# print(list(que))
maxday = 0
lenn = len(que)
if lenn == x * y * z : 
	print(0)
else : 
	while (que):
		oldz, oldy, oldx, oldday = que.popleft() # 0 1 3 1 
		for anc in sign:
			newz = anc[0] + oldz
			newy = anc[1] + oldy
			newx = anc[2] + oldx
			if check_out(newz, newy, newx, z, y, x)== False:
				continue 
			if boxes[newz][newy][newx] == 1 or boxes[newz][newy][newx] == -1:
				continue 
			boxes[newz][newy][newx] = 1
			que.append((newz, newy, newx, oldday+1))
			lenn += 1
			maxday = max(maxday, oldday+1)
		if lenn == z * y * x - cntminus:
			break 
		# print(list(que))
	# print(boxes)
	flag = 1
	for sz in range(z):
		for sy in range(y):
			for i in range(x):
				if boxes[sz][sy][i] == 0:
					flag = -1
	if flag == -1:
		print(-1)
	else:
		print(maxday)