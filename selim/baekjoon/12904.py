# acmicpc.net/problem/12904
# A와 B 

# 12904dfsV는 시간초과로 통과불가. 
# s, t에서 t를 pop하는 방법으로 s를 만들어야 한다 

import sys 

df = 0

def solution(slst, tlst):
	# print(s, t)
	s = list(slst)
	t = list(tlst)
	while (len(s) != len(t)):
		if t[-1] == 'A':
			t.pop()
		else:
			t.pop()
			t = t[::-1]
	if s == t:
		print(1)
	else:
		print(0)
	return 

S = sys.stdin.readline().rstrip()
T = sys.stdin.readline().rstrip()
solution(S, T)
# solution('AB', 'ABB')  0
# solution('BAAB', 'BAABA')  1
# solution('B', 'ABBA') 1