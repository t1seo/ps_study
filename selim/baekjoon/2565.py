# https://www.acmicpc.net/problem/2565
# 전깃줄 

import sys
from collections import deque

def ft_max(a, b):
	if a > b:
		return a 
	return b

def solution(numbers):
	n = len(numbers)
	templst = []
	cnt = 0
	for i in range(n):
		templst.append(0)
	for i in range(n):
		templst[i] = 1
		for j in range(0, i):
			if templst[j] + 1 > templst[i] and numbers[i][1] > numbers[j][1]:
				templst[i] = templst[j] + 1
		cnt = ft_max(cnt, templst[i])
	print(n - cnt)
# def solution1(numbers):
# 	st = len(numbers)
# 	que = deque()
# 	for i, item in enumerate(numbers):
# 		if que and que[-1][1] > item[1]:
# 			while (que and que[-1][1] > item[1]):
# 				que.pop()
# 		que.append(item)
# 	print(st - len(que))

n = sys.stdin.readline()
numbers = []
for i in range(int(n)):
	a, b = sys.stdin.readline().split()
	numbers.append([int(a), int(b)])
numbers.sort()
solution(numbers)

"""
8
1 8
3 9
2 2
4 1
6 4
10 10
9 7
7 6
"""

"""
4
1 1
2 4
3 2
4 3
"""
"""
6
1 8
2 9
4 4
5 2
6 1
7 5
"""

# https://sihyungyou.github.io/baekjoon-2565/ 
# 모범코드 dynamic programming으로 푸는 방법