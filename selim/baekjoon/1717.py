# https://www.acmicpc.net/problem/1717
# 집합의 표현 
# 한번에 통과 / 비슷한 문제 : 2606번 바이러스 union find 

import sys

root = [x for x in range(1000001)]

n, m = map(int, sys.stdin.readline().split())

def find(x):
	if root[x] == x:
		return x
	root[x] = find(root[x])
	return root[x]

def union(x, y):
	x = find(x)
	y = find(y)
	if x != y:
		if y < x:
			root[y] = x
		else:
			root[x] = y

for i in range(m):
	key, x, y = map(int, sys.stdin.readline().split())
	if key == 0:
		union(x, y)
	else:
		if find(x) == find(y):
			print("YES")
		else:
			print("NO")