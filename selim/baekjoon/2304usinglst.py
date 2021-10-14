# https://www.acmicpc.net/problem/2304

import sys

def mountainhgt(n, numlst, ind):
	# 2~7
	# 8~9
	# 9~15
	orglst = []
	answer = 0
	numind = 0
	print(ind)
	maxhgt = numlst[0][1]
	for i in range(numlst[0][0], ind): # 0~7 
		# if i < numlst[numind][0]:
		# 	orglst.append(0)
		# 	continue
		print(i, numlst[numind+1][0])
		if numind+1 < n and i >= numlst[numind+1][0]:
			numind += 1
		print(i, numlst[numind][1], maxhgt)
		if numlst[numind][1] > maxhgt:
			maxhgt = numlst[numind][1]
			print("changed maxhgt", maxhgt)
		orglst.append(maxhgt)
		answer += maxhgt
	numind += 1
	orglst.append(numlst[numind][1])
	answer += numlst[numind][1]
	print(orglst)
	numind = n-1
	secndlst = []
	maxhgt = numlst[numind][1]
	for i in range(numlst[numind][0], ind, -1):
		# print(i)
		if i > numlst[numind][0]:
			secndlst.append(0)
			continue
		if numind-1 >= 0 and i <= numlst[numind-1][0]:
			numind -= 1
		print(i, numlst[numind][1], maxhgt)
		if numlst[numind][1] > maxhgt :
			maxhgt = numlst[numind][1]
			print("changedmaxhgt", maxhgt)
		secndlst.append(maxhgt)
		answer += maxhgt
	print(secndlst)
	summ = sum(orglst) + sum(secndlst)
	print(summ)
	print(answer)

def trapezoidhgt(n, numlst, sta, lst):
	# 2~7
	# 8~10
	# 11~15
	orglst = []
	answer = 0
	numind = 0
	print(sta,lst)
	maxhgt = numlst[0][1]
	for i in range(numlst[0][0], sta): # 0~7 
		# if i < numlst[numind][0]:
		# 	orglst.append(0)
		# 	continue
		print(i, numlst[numind+1][0])
		if numind+1 < n and i >= numlst[numind+1][0]:
			numind += 1
		print(i, numlst[numind][1], maxhgt)
		if numlst[numind][1] > maxhgt:
			maxhgt = numlst[numind][1]
			print("changed maxhgt", maxhgt)
		orglst.append(maxhgt)
		answer += maxhgt
	numind += 1
	for i in range(sta, lst+1): # 8~10
		orglst.append(numlst[numind][1])
		answer += numlst[numind][1]
	print(orglst)
	numind = n-1
	secndlst = []
	maxhgt = numlst[numind][1]
	for i in range(numlst[numind][0], lst, -1):
		# print(i)
		if i > numlst[numind][0]:
			secndlst.append(0)
			continue
		if numind-1 >= 0 and i <= numlst[numind-1][0]:
			numind -= 1
		print(i, numlst[numind][1], maxhgt)
		if numlst[numind][1] > maxhgt :
			maxhgt = numlst[numind][1]
			print("changedmaxhgt", maxhgt)
		secndlst.append(maxhgt)
		answer += maxhgt
	print(secndlst)
	summ = sum(orglst) + sum(secndlst)
	print(summ)
	print(answer)


def solution(n, numlst):
	hgtslst = []
	for i in range(n):
		hgtslst.append(numlst[i][1])
	maxhgt = max(hgtslst)
	cnt = hgtslst.count(maxhgt)
	if (cnt == 1): # mountain 
		ind = hgtslst.index(maxhgt) # 8
		mountainhgt(n, numlst, numlst[ind][0])
	else:
		sta = hgtslst.index(maxhgt)
		ed = list(reversed(hgtslst)).index(maxhgt)
		print("staed", sta, n - ed - 1)
		trapezoidhgt(n, numlst, numlst[sta][0], numlst[n-ed-1][0])
# n = int(input())
# numlst = []
# for i in range(n):
# 	a, b = sys.stdin.readline().split()
# 	numlst.append([int(a), int(b)])
# numlst.sort()
# print(numlst)

numlst = [[2, 4], [4, 6], [5, 3], [8, 10], [9, 10], [11, 4], [13, 6], [15, 8]]

solution(len(numlst), numlst)
# print(4+4+6*4+10+8*7)