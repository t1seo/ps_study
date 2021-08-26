# acmicpc.net/problem/2491
# 다이나믹 프로그래밍 > 수열 

def solution(n, lst):
	# print(lst)
	upold, downold = 0, 0
	upcnt, downcnt = 0, 0
	maxx = 0
	for i in range(n):
		if (upold <= lst[i]): # 오름차순으로 카운트 
			upold = lst[i]
			upcnt += 1
			maxx = max(maxx, upcnt)
		else:					# 연이어서 오르지 않을 때 초기화 
			upold = lst[i]
			upcnt = 1
		if (downold <= lst[n-1-i]): # 내림차순 카운트
			downold = lst[n-1-i]
			downcnt += 1
			maxx = max(maxx, downcnt)
		else:					# 마찬가지로 연이어서 오르지 않을 떄 초기화
			downold = lst[n-1-i]
			downcnt = 1
	print(maxx)

n = input()
k = list(map(int, input().split()))
solution(int(n), k)
# solution(9, [1, 2, 2, 4, 4, 5, 7, 7, 2])