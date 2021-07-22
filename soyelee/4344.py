c = int(input())
for i in range(0, c):
	n = list(map(int, input().split()))
	score = 0
	students = 0
	for j in range(0, n[0]):
		score += n[j + 1]
	score = score / n[0]
	for k in range(0, n[0]):
		if n[k + 1] > score:
			students += 1
	print('%.3f%%'%(students * 100 / n[0]))
