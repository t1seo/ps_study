# https://www.acmicpc.net/problem/19598
# 최소 회의실 개수 

from collections import deque 
from functools import cmp_to_key
import sys 

def solution(lst):
	dq = []
	for i in range(len(lst)):
		dq.append([lst[i][0], 1]) # start는 1을 함께 
		dq.append([lst[i][1], -1]) # end 는 -1을 함께 묶어서 dq list에 넣는다 (deque X)
	dq.sort()
	# print(dq)
	cnt = 0
	maxx = 1
	for i in range(len(dq)):
		cnt += dq[i][1] 		# dq[i][1] 값은 start면 1을 더하고 end면 -1을 더한다. 
		maxx = max(maxx, cnt) 	# 가장 많이 회의가 겹치는 순간의 방 개수가 maxx에 담겨진다. 
	print(maxx)	#답

numbers = []
n = int(sys.stdin.readline())
for i in range(n):
	a, b = sys.stdin.readline().split()
	numbers.append([int(a),int(b)])
solution(numbers)


# 참고
# https://jminie.tistory.com/7


# 기존 코드 문제 이해를 잘못했었음. 
# 하지만 key=cmp_to_key 를 썼던 코드는 남겨두고 싶어서 주석으로 남겨놓기 
# def compare(item1, item2):
# 	if item1[0] < item2[0]:
# 		return -1
# 	elif item1[0] > item2[0]:
# 		return 1
# 	if item1[1] > item2[1]:
# 		return 1
# 	elif item1[1] < item2[1]:
# 		return -1
# 	return 0
	
# def solution1(lst):
# 	numbers = sorted(lst, key=cmp_to_key(compare))
# 	dq = deque()
# 	dq.append(numbers[0][1]) # end 
# 	maxx = 1
# 	print(numbers)
# 	for i in range(1, len(numbers)):
# 		if dq[0] <= numbers[i][0]:
# 			dq.popleft()
# 			dq.append(numbers[i][1])
# 		else:
# 			dq.append(numbers[i][1])
# 	print(dq)
# 	print(len(dq))

