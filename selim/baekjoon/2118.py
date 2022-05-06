import sys 
input = sys.stdin.readline
n = int(input())
data = []
for i in range(n):
	data.append(int(input()))
# data = range(1,6)
# print(data)
best = sum(data)/2
s, e = 0, 1
nujuk = data[0]
answer = 0
while e <= len(data): 
	if nujuk <= best : 
		e += 1
		if e > len(data):
			break
		nujuk += data[e-1]
	else : 
		answer = max(answer, min(nujuk, sum(data)-nujuk))
		nujuk -= data[e-1]
		answer = max(answer, min(nujuk, sum(data)-nujuk))
		s += 1
		nujuk = nujuk + data[e-1] - data[s-1]
		# answer = max(answer, min(nujuk, sum(data)-nujuk))
print(answer)
