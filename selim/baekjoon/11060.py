# https://www.acmicpc.net/problem/11060
# 다이나믹 > 점프점프 
from collections import deque

def solution(n, arr):
	bucket = [0 for i in range(n+101)]
	# print(bucket)
	bucket[0] = 1
	if n == 1:
		print("0")
		return 
	if arr[0] == 0:
		print("-1")
		return
	for i in range(0, n):
		for j in range(1, arr[i]+1): # 1, 2, 3
			if i + j < n and bucket[i] != 0:
				if bucket[i+j] != 0:
					bucket[i+j] = min(bucket[i+j], bucket[i]+1)
				else:
					bucket[i+j] = bucket[i] +1
	# print(bucket)
	if bucket[n-1] != 0:
		print(bucket[n-1]-1)
	else:
		print("-1")
	return

n = int(input())
arr = []
arr = input().split()
arr = map(int, arr)
solution(n, list(arr))

# solution(10, [1, 2, 0, 1, 3, 2, 1, 5, 4, 2])
# solution(10, [1, 1, 0, 1, 1, 1, 1, 1, 1, 1])
# solution(2, [2, 0])
# solution(2, [0, 2])
# solution(2, [1, 2])
# solution(1, [0])

"""que로 풀었더니 메모리 초과가 떴다 """
# def solution(n, arr):
# 	# print(n, arr)
# 	# bucket = [[0 for i in range(n+1)] for j in range(n+1)]
# 	# print(len(bucket))

# 	que = deque()
# 	answerList = set()
# 	que.append((0, 0, 0))
# 	while que:
# 		oldx , oldy, oldlev = que.popleft()
# 		for i in range(1, arr[oldx]+1):
# 			newx = oldx + i
# 			if newx >= n:
# 				# answerList.add(oldlev+1)
# 				print(oldlev+1)
# 				return 
# 			elif arr[newx] == 0:
# 				continue
# 			else : 
# 				que.append((newx, 0, oldlev+1))
# 	# print(answerList)
# 	if len(answerList) == 0:
# 		print("-1")
# 		return 
# 	print(min(answerList))
# 	return 
