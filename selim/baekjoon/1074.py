# https://www.acmicpc.net/problem/1074
# Z (재귀)
import sys 
import math

summ = 0

def addnum(totallen, r, c) : 
	global summ 
	if r == 0 and c == 0:
		return summ 
	elif r == 0 and c == 1:
		summ += 1
		return summ 
	elif r == 1 and c == 0:
		summ += 2
		return summ
	elif r == 1 and c == 1: 
		summ += 3
		return summ 
	
	if r >= totallen // 2:
		smallhalf = (totallen // 2)*(totallen //2)
		summ += smallhalf * 2
		r -= totallen // 2
	
	if c >= totallen // 2:
		smallhalf = (totallen // 2)*(totallen //2)
		summ += smallhalf
		c -= totallen // 2
	addnum(totallen / 2, r, c)
	return summ


def solution(N, r, c):
	global summ
	totallen = math.pow(2, N)
	addnum(totallen, r, c)
		

N, r, c = map(int, sys.stdin.readline().split())
solution(N, r, c)
print(int(summ))
# solution(2, 3, 1)
# solution(3, 7, 7)
# solution(1, 0, 0)
# solution(4, 7, 7)
# solution(10, 511, 511)