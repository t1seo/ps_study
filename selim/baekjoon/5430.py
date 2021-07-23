# https://www.acmicpc.net/problem/5430
import sys
from collections import deque

def AC(p, lenn, arr): # RDD 4 [1,2,3,4]
	i = 0	# 
	r = 0
	if (arr[0] == '' and p[0] == 'D'):
		print("error")
		return 
	while (p[i] == 'R' or p[i] == 'D'): # 3 
		if (p[i] == 'R'):
			r += 1
		elif (len(arr) == 0 and p[i] == 'D'):
			print("error")
			return 
		else:
			if (r % 2 == 0):
				arr.pop(0)
			else:
				arr.pop()
		i += 1
	arr = list(arr)
	if (r % 2 == 1):
		arr.reverse()
	print('[', end = '')
	for i in range(len(arr)):
		print(arr[i], end = '')
		if (i != len(arr)-1):
			print(',', end = '')
	print(']')

n = int(sys.stdin.readline())
for i in range(n):
	p = sys.stdin.readline()
	k = int(sys.stdin.readline()) # sys.stdin.readline().rstrip()
	arr = sys.stdin.readline()[1:-2].split(",")
	AC(p, k, arr)

"""
1
D
0
[] ?? error https://www.acmicpc.net/board/view/68882
"""