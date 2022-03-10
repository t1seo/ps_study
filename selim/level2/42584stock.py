# https://programmers.co.kr/learn/courses/30/lessons/42584#
# 스택/큐 > 주식가격

from collections import deque

def solution1(prices):
    answer = []
    for i in range(len(prices)):
        answer.append(0)
    que = deque()
    lenn = len(prices)
    for i in range(lenn): # 스택 / 큐 
        while que and prices[que[-1]] > prices[i]:
            top = que.pop()
            answer[top] = i - top
        que.append(i)
    while (que):
        top = que.pop() 
        answer[top] = lenn - 1 - top
    return answer

def solution(prices):
    answer = [0] * len(prices)
    for i in range(len(prices)): # 2중 for문 앞에서 읽어나가고 뒤를 확인 
        for j in range(i+1, len(prices)):
            if prices[i] <= prices[j]:
                answer[i] += 1
            else:
                answer[i] += 1
                break
    return answer



# def practice1(prices):
# 	que = deque()
# 	lenn = len(prices) # 5
# 	timee = [0] * lenn 
# 	for i in range(lenn):
# 		if len(que) == 0:
# 			que.append((prices[i], i))
# 		elif que[-1][0] <= prices[i]: 
# 			que.append((prices[i], i))
# 		else : 
# 			while que[-1][0] > prices[i]:
# 				rc = que.pop()
# 				print(rc)
# 				que.append((prices[i], i))
# 		print(que)