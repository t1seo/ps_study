import math

n = int(input())
a = list(map(int, input().split()))
count = 0
for i in a:
    flag = 0
    if i > 1:
        if i == 2 or i == 3:
            count += 1
        else:
            for j in range(2, int(math.sqrt(i)) + 1):
                if i % j == 0:
                    flag = 1
            if flag == 0:
                count += 1
print(count)

# https://www.acmicpc.net/board/view/65480
# range(2, int(math.sqrt(i)) + 1)
