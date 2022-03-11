# acmicpc.net/problem/14889
# 스타트와 링크 
from itertools import combinations

import sys
input = sys.stdin.readline

n = int(input())
lst = []
for i in range(n):
	a = list(map(int, input().split()))
	lst.append(a)
members = [i for i in range(n)]
pos_team = []
for team in list(combinations(members, n//2)):
	pos_team.append(team)

min_gap = 10000
for i in range(len(pos_team)//2):
	ateam = pos_team[i]
	stat_a = 0
	for j in range(n//2):
		member = ateam[j]
		for k in ateam:
			stat_a += lst[member][k]

	bteam = pos_team[-i-1]
	stat_b = 0
	for j in range(n//2):
		member = bteam[j]
		for k in bteam:
			stat_b += lst[member][k]
	
	min_gap = min(min_gap, abs(stat_a - stat_b))
print(min_gap)