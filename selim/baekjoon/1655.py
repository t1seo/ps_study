# acmicpc.net/problem/1655
# 가운데를 말해요 
# https://art-coding3.tistory.com/44 GOOD 

import sys 
import heapq

n = int(sys.stdin.readline())
max_heap = []
heapq.heapify(max_heap) # 0~ mid should be max_heap
min_heap = []
heapq.heapify(min_heap) # mid ~ end should be min_heap
answer = []

for i in range(n):
	newn = int(sys.stdin.readline())

	if len(max_heap) == len(min_heap):
		heapq.heappush(max_heap, (-newn, newn)) # to make max heap, (-newn) needed
	else:
		heapq.heappush(min_heap, (newn, newn))
	
	if min_heap and max_heap[0][1] > min_heap[0][1]:
		minn = heapq.heappop(min_heap)[1]
		maxx = heapq.heappop(max_heap)[1]
		heapq.heappush(max_heap, (-minn, minn))
		heapq.heappush(min_heap, (maxx, maxx))
	
	answer.append(max_heap[0][1])
for j in answer:
	print(j)
