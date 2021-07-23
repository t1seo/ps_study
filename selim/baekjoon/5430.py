# https://www.acmicpc.net/problem/5430
import sys
from collections import deque

def AC(p, lenn, arr): # RDD 4 [1,2,3,4]
	i = 0	# p의 인덱스
	r = 0	# reverse의 count
	if (arr[0] == '' and p[0] == 'D'): # 예외처리 1 D 0 [] 일 경우 error가 나와야 한다 
		print("error")
		return 
	while (p[i] == 'R' or p[i] == 'D'): # len(p)로 하면 오류가 난다 
		if (p[i] == 'R'): # 바로바로 reverse()하면 시간초과가 나므로 r로 카운트만 한다 
			r += 1
		elif (len(arr) == 0 and p[i] == 'D'): # arr에 아무것도 없는데 D를 하라고 하면 error
			print("error")
			return 
		else:
			if (r % 2 == 0): # r이 짝수면 맨 앞에 숫자를 빼기
				arr.pop(0)
			else:			 # r이 홀수면 맨 뒤에 숫자를 뺴기 
				arr.pop()
		i += 1
	arr = list(arr)			# 디큐-> 리스트 
	if (r % 2 == 1):		# r 홀짝에 따라 reverse를 실시 
		arr.reverse()
	
	print('[', end = '')	# 프린트 ['1', '2']가 아니라 [1,2]로 프린트되도록 
	for i in range(len(arr)):
		print(arr[i], end = '')
		if (i != len(arr)-1):
			print(',', end = '')
	print(']')

n = int(sys.stdin.readline())
for i in range(n):
	p = sys.stdin.readline()
	k = int(sys.stdin.readline()) # sys.stdin.readline().rstrip()
	arr = sys.stdin.readline()[1:-2].split(",")
	AC(p, k, arr)

"""
1
D
0
[] 
?? error가 프린트되어야 한다 https://www.acmicpc.net/board/view/68882
"""