# https://www.acmicpc.net/problem/9465
# 스티커 

import sys

maxx = 0

def dfs(n, numbers, lev, summ, topbot):
	global maxx
	if (n <= lev):
		# print('here', maxx, summ)
		if (maxx < summ):
			maxx = summ
			# print(maxx)
		return 
	# print(lev, summ, maxx)
	if (topbot[0] == 0):
		dfs(n, numbers, lev + 1, summ + numbers[0][lev], [1,0])
	if (topbot[1] == 0):
		dfs(n, numbers, lev + 1, summ + numbers[1][lev], [0,1])
	if (lev + 2 <= n):
		dfs(n, numbers, lev + 1, summ, [0, 0])
	return 
		

def solution(n, numbers):
	# print(numbers)
	topbot = [0,0]
	summ = 0
	dfs(n, numbers, 0, summ, topbot)
	dfs(n, numbers, 1, summ, topbot)
	print(maxx)
	# print(df1, df2)


k = int(sys.stdin.readline())
for i in range(k):
	n = int(sys.stdin.readline())
	numbers = []
	for _ in range(2):
		temp = map(int, sys.stdin.readline().split())
		numbers.append(list(temp))
	solution(n, numbers)
# solution(5, [[50, 10, 100, 20, 40], [30, 50, 70, 10, 60]])

"""
1
5
50 10 100 20 40
30 50 70 10 60
"""