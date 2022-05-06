import bisect

n = int(input())
an = list(map(int, input().split()))

arr = []
cnt = 0
for item in an:
	if len(arr) == 0:
		arr.append(item)
		cnt += 1
		continue 
	if arr[-1] < item : 
		arr.append(item)
		cnt += 1
	else : 
		ind = bisect.bisect_left(arr, item)
		arr[ind] = item
print(cnt)



