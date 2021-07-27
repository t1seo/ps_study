x, y = map(int, input().split())
line_x = [0, x]
line_y = [0, y]
for _ in range(int(input())):
    direction, line = map(int, input().split())
    if direction:
        line_x.append(line)
    else:
        line_y.append(line)
line_x.sort()
line_y.sort()
max_x = 0
max_y = 0
for i in range(1, len(line_x)):
    if line_x[i] - line_x[i - 1] > max_x:
        max_x = line_x[i] - line_x[i - 1]
for j in range(1, len(line_y)):
    if line_y[j] - line_y[j - 1] > max_y:
        max_y = line_y[j] - line_y[j - 1]
print(max_x * max_y)

# https://www.acmicpc.net/source/22690596
"""
for i in range(len(y)-1):
    for j in range(len(x)-1):
        res.append((y[i+1]-y[i])*(x[j+1]-x[j]))
print(max(res))
"""
