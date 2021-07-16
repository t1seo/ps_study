# https://www.acmicpc.net/problem/6198
# 옥상정원 꾸미기 
from collections import deque
import sys 

def solution(number):
	if (len(number) == 1):
		return (0)
	stack = deque()
	sumup = 0
	for i in range(len(number)):
		while (stack and stack[-1] <= number[i]):
			stack.pop()
		stack.append(number[i])
		sumup += len(stack) - 1
	return (sumup)
	

n = int(sys.stdin.readline())
lst = []
for i in range(n):
	tmp = int(sys.stdin.readline())
	lst.append(tmp)
print(solution(lst))


# def solution1(number):
# 	if (len(number) == 1):
# 		return (0)
# 	max = number[-1]
# 	sumup = 0
# 	lenn = len(number)
# 	for i in range(lenn - 2, -1, -1):
# 		if (max < number[i]):
# 			sumup += lenn - i - 1
# 			max = number[i]
# 		else : 
# 			for k in range(i + 1, lenn):
# 				if number[k] >= number[i]:
# 					break 
# 				else : 
# 					sumup += 1
# 	return (sumup)
