# https://www.acmicpc.net/problem/2606
# 바이러스 union find 알고리즘 
import sys 

root = [x for x in range(101)]

def find(x):
	if root[x] == x:
		return x
	else:
		root[x] = find(root[x])
		return root[x]

def union(x, y):
	parx = find(x)
	pary = find(y)
	if (parx != pary):
		root[pary] = parx

n = int(sys.stdin.readline())
k = int(sys.stdin.readline())
for i in range(k):
	x, y = map(int, sys.stdin.readline().split())
	union(x, y)

summ = 0
for i in range(2, n+1):
	if find(1) == find(i): # root[1] == root[i] 였는데 둘다 find()여야지 옳은 풀이. 
		summ += 1
print(summ)
# for i in range(1, n+1): # 이렇게 되면 뒤 늦게 이어지는 애들도 가장 윗 애로 이어짐 
# 	print(root[i], end = ' ')

"""반례 #https://www.acmicpc.net/board/view/71786
7
6
2 3
1 2
1 5
5 2
5 6
4 7
"""