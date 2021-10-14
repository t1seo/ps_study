# https://www.acmicpc.net/problem/2304

import sys

def mountainhgt(n, numlst, nind):
	# 2~7
	# 8~9
	# 9~15
	ind = numlst[nind][0]
	answer = 0
	numind = 0
	maxhgt = numlst[0][1]
	for i in range(numlst[0][0], ind): # 0~7 
		if numind+1 < n and i >= numlst[numind+1][0]:
			numind += 1
		if numlst[numind][1] > maxhgt:
			maxhgt = numlst[numind][1]
		answer += maxhgt
	answer += numlst[nind][1]
	numind = n-1
	maxhgt = numlst[numind][1]
	for i in range(numlst[numind][0], ind, -1):
		if numind-1 >= 0 and i <= numlst[numind-1][0]:
			numind -= 1
		if numlst[numind][1] > maxhgt :
			maxhgt = numlst[numind][1]
		answer += maxhgt
	print(answer)

def trapezoidhgt(n, numlst, nsta, nlst):
	# 2~7
	# 8~10
	# 11~15
	sta = numlst[nsta][0]
	lst = numlst[nlst][0]
	answer = 0
	numind = 0
	maxhgt = numlst[0][1]
	for i in range(numlst[0][0], sta): # 0~7 
		if numind+1 < n and i >= numlst[numind+1][0]:
			numind += 1
		if numlst[numind][1] > maxhgt:
			maxhgt = numlst[numind][1]
		answer += maxhgt
	for i in range(sta, lst+1): # 8~10
		answer += numlst[nsta][1]
	numind = n-1
	maxhgt = numlst[numind][1]
	for i in range(numlst[numind][0], lst, -1):
		if numind-1 >= 0 and i <= numlst[numind-1][0]:
			numind -= 1
		if numlst[numind][1] > maxhgt :
			maxhgt = numlst[numind][1]
		answer += maxhgt
	print(answer)


def solution(n, numlst):
	if (n == 1):
		print(numlst[0][1])
		return 
	if (n == 2):
		print(numlst[0][1] + numlst[1][1])
		return 
	hgtslst = []
	for i in range(n):
		hgtslst.append(numlst[i][1])
	maxhgt = max(hgtslst)
	cnt = hgtslst.count(maxhgt)
	if (cnt == 1): # mountain 
		ind = hgtslst.index(maxhgt) # 8
		mountainhgt(n, numlst, ind)
	else:
		sta = hgtslst.index(maxhgt)
		ed = list(reversed(hgtslst)).index(maxhgt)
		trapezoidhgt(n, numlst, sta, n - ed - 1)
n = int(input())
numlst = []
for i in range(n):
	a, b = sys.stdin.readline().split()
	numlst.append([int(a), int(b)])
numlst.sort()
# print(numlst)

# numlst = [[2, 4], [4, 6], [5, 3], [8, 10], [9, 10], [11, 4], [13, 6], [15, 8]]

solution(len(numlst), numlst)
# print(4+4+6*4+10+8*7)