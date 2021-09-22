"""
acmicpc.net/problem/10953
A+B-6
"""

n = int(input())
for i in range(n):
	lne = list(map(int,input().split(',')))
	print(lne[0]+lne[1])
