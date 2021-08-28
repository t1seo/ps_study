# https://www.acmicpc.net/problem/16198
# 백트랙킹, 재귀 > 에너지 모으기

finsumlst = []

def dfs(numbers, sum, n): 
	if (n == 2):
		finsumlst.append(sum)
		return 
	tmpsum = 0
	savenum = 0
	for i in range(1, n-1): # 1,2, ... n-2
		tmpsum = numbers[i-1]*numbers[i+1]
		savenum = numbers[i]
		del numbers[i]
		dfs(numbers, sum + tmpsum, n-1)
		numbers.insert(i, savenum)
		
def solution(n, numbers):
	# print(numbers)
	sum = 0
	if (n < 3):
		print(-1)
		return 
	dfs(numbers, sum, n)
	print(max(finsumlst))

n = input()
tmp = map(int, input().split())
solution(int(n), list(tmp))