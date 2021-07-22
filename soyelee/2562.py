maximum = 0;
index = 0;
for i in range(0, 9):
	n = int(input())
	if maximum < n:
		maximum = n
		index = i + 1
print(maximum)
print(index)
