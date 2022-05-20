import sys 
input = sys.stdin.readline
n = int(input())
lines = []
for i in range(n):
    lines.append(list(map(int, input().split())))
lines.sort()
# print(lines)

dp = [1] * n 
for i in range(n):
    for j in range(i):
        if lines[i][1] > lines[j][1] and dp[i] < dp[j] +1:
            # print(i, dp[i], dp[j] + 1)
            dp[i] = dp[j] + 1 
# print(dp)
print(n - max(dp))