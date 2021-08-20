# https://www.acmicpc.net/problem/9465
# 스티커 

import sys

def solution(n, dp):
	if (n == 1):
		print(max(dp[0][0], dp[1][0]))
		return
	dp[0][1] += dp[1][0]
	dp[1][1] += dp[0][0]

	for i in range(2, n):
		dp[0][i] += max(dp[1][i - 1], dp[1][i - 2])
		dp[1][i] += max(dp[0][i - 1], dp[0][i - 2])
	print(max(dp[0][n-1], dp[1][n-1]))






k = int(sys.stdin.readline())
for i in range(k):
	n = int(sys.stdin.readline())
	dp = []
	for _ in range(2):
		temp = map(int, sys.stdin.readline().split())
		dp.append(list(temp))
	solution(n, dp)