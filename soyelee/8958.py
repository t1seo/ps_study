n = int(input())
for i in range(0, n):
	score = 0
	add = 0;
	testcase = input()
	for j in range(0, len(testcase)):
		if testcase[j] == 'O':
			add += 1
			score += add
		else:
			add = 0
	print(score)
