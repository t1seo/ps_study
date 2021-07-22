a = int(input())
b = int(input())
c = int(input())
abc = a * b * c
count = [0] * 10
while abc != 0:
	n = abc % 10
	abc = int(abc / 10)
	count[int(n)] += 1
for i in range(0, 10):
	print(count[i])
