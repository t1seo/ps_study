# acmicpc.net/problem/12904
# A와 B 

# 이 코드는 시간초과로 통과못했지만 아쉬워서 남기는 파일 

import sys 

def comparest(s, t):
	for i in range(len(s)):
		if s[len(s) - i - 1] != t[i]:
			return 0
	return 1

def dfs(s, t, slen, tlen, r):
	# print(s)
	if (slen == tlen):
		if r == -1:
			return comparest(s, t)
		if s == t:
			return 1
		else:
			return 0
	if (r == 1):
		df = dfs(s + 'A', t, slen + 1, tlen, r)
		if df == 1:
			return df
		df = dfs('B' + s, t, slen + 1, tlen, r * -1)
		if df == 1:
			return df
	if (r == -1):
		df = dfs('A' + s, t, slen + 1, tlen, r)
		if df == 1:
			return df
		df = dfs(s + 'B', t, slen + 1, tlen, r * -1)
		if df == 1:
			return df	
	return 0


def solution(s, t):
	# print(s, t)
	r = 1 # reverse 
	pos = dfs(s + 'A', t, len(s) + 1, len(t), 1)
	if pos == 1:
		print(pos)
		return 
	pos = dfs(''.join(reversed(s)) + 'B', t, len(s) + 1, len(t), 1)
	print(pos)
	return 

S = sys.stdin.readline().rstrip()
T = sys.stdin.readline().rstrip()
solution(S, T)
# solution('AB', 'ABB')
# solution('BAAB', 'BAABA')
# solution('B', 'ABBA')