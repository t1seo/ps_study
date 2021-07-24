import math


def prime(n):
    if n == 1:
        return 0
    if n == 2 or n == 3:
        return 1
    for j in range(2, int(math.sqrt(n)) + 1):
        if n % j == 0:
            return 0
    return 1


t = int(input())
for _ in range(t):
    n = int(input())
    i = n / 2
    while i > 1:
        if prime(i) == 1 and prime(n - i) == 1:
            break
        i -= 1
    print(int(i), int(n - i))

# while i > 1
# ->
# for i in range(n / 2, 0, -1)
# 	: range(start, end, step)
