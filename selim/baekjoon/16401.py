# https://www.acmicpc.net/problem/16401
import sys
input = sys.stdin.readline
m, n = map(int, input().split())
arr = list(map(int, input().split()))

arr = sorted(arr, reverse=True)
answer = 0
left = 1
right = arr[0] #가장 긴 막대 길이 
while (left <= right):
	mid = (left + right) // 2 # 중간 막대 길이 
	cnt = 0
	for a in arr:
		cnt += a // mid 
		if cnt >= m: # 과자를 다 안돌아도 조카 수를 충족하면
			break 
	# print('left:', left, 'right:', right, 'mid:', mid, 'cnt:', cnt)
	if cnt >= m:
		answer = mid
		left = mid+1 # 최대값을 찾을 것이므로 mid보다 더 큰 범위 탐색 
	else:
		right = mid-1 # 아직 막대 길이가 너무 기므로 더 작은 범위에서 탐색 
print(answer)
"""
예외처리 확인 
3 2 
1 1 
answer : 0
"""