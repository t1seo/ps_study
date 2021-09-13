# https://www.acmicpc.net/problem/22233
# 가희와 키워드
# 처음에 set의 함수 difference로 차집합으로 풀려고 했지만 시간초과 
# dict[keys] = 1 로 연산해서 하는 방법으로 노선을 틀어서 맞았다. 


import sys

keysn, writings = map(int, sys.stdin.readline().split())
keyw = {}
for i in range(keysn):
	keyw[sys.stdin.readline().rstrip()] = 1
# keysn, writings = 5, 2
# keyw = ["map", "set", "dijkstra", "floyd", "os"]
N = len(keyw)
for j in range(writings):
	key2 = sys.stdin.readline().rstrip().split(',')
	# result = list(set(keyw).difference(key2))
	# keyw=result
	for x in key2:
		if x not in keyw.keys():
			continue
		if keyw[x] == 1:
			keyw[x] = 0
			N -= 1
	print(N)