# https://www.acmicpc.net/problem/11478
# 서로 다른 문자열의 개수 

def solution(longstr, n):
	# print(longstr)
	fst = len(set(longstr))
	tmpstr = ""
	summ = fst + 1
	for i in range(2, n):
		tmpset = set()
		for j in range(0, n-i+1):
			tmpstr = longstr[j:j+i]
			tmpset.add(tmpstr)
		# print(tmpset)
		summ += len(tmpset)
	print(summ)


tmp = input()
solution(tmp, len(tmp))