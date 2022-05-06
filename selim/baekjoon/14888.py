import sys 
input = sys.stdin.readline

n = int(input())
alst = list(map(int, input().split())) # 5, 6
ops = list(map(int, input().split())) # 0 0 1 0 

maxminlst = [float('-inf'), float('inf')]

def dfs(lev, summ):
	if lev == len(alst):
		maxminlst[0] = max(maxminlst[0], summ)
		maxminlst[1] = min(maxminlst[1], summ)
		return 
	if ops[0] >= 1:
		ops[0] -= 1 
		newsum = summ + alst[lev]
		dfs(lev+1, newsum)
		ops[0] += 1
	if ops[1] >= 1:
		ops[1] -= 1
		newsum = summ - alst[lev]
		dfs(lev+1, newsum)
		ops[1] += 1
	if ops[2] >= 1:
		ops[2] -= 1 
		newsum = summ * alst[lev]
		dfs(lev+1, newsum)
		ops[2] += 1
	if ops[3] >= 1:
		ops[3] -= 1
		if summ < 0: # C++14 method
			newsum = (-summ) // alst[lev]
			newsum *= -1
		else:
			newsum = summ // alst[lev]
		dfs(lev+1, newsum)
		ops[3] += 1

dfs(1, alst[0])
print(maxminlst[0])
print(maxminlst[1])
# print(3 // 4)