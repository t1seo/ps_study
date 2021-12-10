# https://www.acmicpc.net/problem/1202
# 그리디 > 보석 도둑 

import sys 
import heapq
import queue

"""similar
12978delivery.py
42626spicy.py 
"""

def solution(n, k, narr):
	answer = 0
	pq = queue.PriorityQueue(n)
	narr.sort()
	# print(narr)
	for item in narr:
		if item[1] != 2000000:  # 가방이 아닌 경우 값에 음수를 곱한 값을 넣는다 
			pq.put(-item[1])
		elif (not(pq.empty())): # 가방인 경우, 그리고 pq에 값이 있을 때 
			th = -pq.get()		# 뒤집어놓았던 값을 더한다. 
			answer += th
	print(answer)
	

# def solution1(n, k, marr, carr):
# 	marr.sort(reverse=True)
# 	carr.sort(reverse=True)
# 	# print(marr)
# 	i = 0
# 	j = 0
# 	visited = [0] * k 
# 	while True : 
# 		if i >= k or j >= n : 
# 			break
# 		if carr[i] >= marr[j][1]: # 10 >= 2 
# 			visited[i] = marr[j][0] # 0 -> 99 
# 			i += 1
# 			j += 1
# 		else : 
# 			j += 1 # marr += 1

# 	print(sum(visited))

n, k = map(int, sys.stdin.readline().split())
marr = []
for i in range(n):
	m, v = sys.stdin.readline().split()
	marr.append((int(m), int(v)))
for i in range(k):
	c = sys.stdin.readline()
	marr.append((int(c), 2000000))

solution(n, k, marr)
# solution(2, 1, [(10, 5), (100, 100)] ,[11])
# solution(3, 2, [(65, 1), (23, 5), ( 99, 2)], [10, 2])