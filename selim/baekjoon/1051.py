# https://www.acmicpc.net/problem/1051
# 브루트포스 알고리즘 > 숫자 정사각형 
maxx = 1

def check_four(y, x, numbers, i):
	std = numbers[y][x]
	if (std != numbers[y+i][x]):
		return 0
	elif (std != numbers[y][x+i]):
		return 0
	elif (std != numbers[y+i][x+i]):
		return 0
	return 1

def solution(n, m, numbers):
	# print(n, m, numbers)
	global maxx
	if (n == 1 or m == 1):
		maxx = 1
		return 1
	for i in range(1, min(n, m)): # 1, 2
		for y in range(0, n-i):
			for x in range(0, m-i):
				if (check_four(y, x, numbers, i) == 1):
					if maxx < i+1:
						maxx = i+1

n, m = map(int, input().split())
numbers = []
for i in range(n):
	tmp = input()
	lst = []
	for j in range(m):
		lst.append(int(tmp[j]))
	numbers.append(lst)
solution(n, m, numbers)
# solution(3, 5, [[4, 2, 1, 0, 1], [2, 2, 1, 0, 0], [2, 2, 1, 0, 1]])
print(maxx**2)