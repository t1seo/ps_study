x, y, w, h = map(int, input().split())
if x > w - x:
	x = w - x
if y > h - y:
	y = h - y
if x > y:
	print(y)
else:
	print(x)
