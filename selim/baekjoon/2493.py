# https://www.acmicpc.net/problem/2493
# 스택/큐 > 탑 

import sys 
from collections import deque


def solution(numbers):
	answer = [0] * len(numbers) 				# 답을 저장하는 리스트 
	dq = deque()
	for i in range(len(numbers) - 1, -1, -1):	# 거꾸로 읽어나간다 
		curr = numbers[i]						# 현재 층의 값 = curr 
		while dq and dq[-1][0] < curr : 		# 스택 값이 작으면 
			answer[dq[-1][1]] = i + 1			# 해당 스택값의 인덱스를 curr로 바꾸고 
			dq.pop()							# 작은 값은 탈출시킨다 
		dq.append([curr, i])					# 그리고 큰 값을 다시 스택에 넣는다 
	
	for i in range(len(answer)):
		print(answer[i], end = ' ')

# 처음에 print(answer)로 [리스트] 자체를 프린트해서 틀렸었음. 로직은 처음부터 맞았다! 


n = int(sys.stdin.readline())
numbers = list(map(int, input().split()))
solution(numbers)
