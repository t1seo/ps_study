# https://programmers.co.kr/learn/courses/30/lessons/12899
# 연습문제 > 124 나라의 숫자 

import sys 

str = "0124"

def solution(n):
	if (n <= 3):
		return str[n]
	
	q = n // 3
	r = n % 3
	return solution(q) + str[r]

y = sys.argv[1]
abc = solution(int(y))
print(abc)