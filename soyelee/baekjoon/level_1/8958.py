n = int(input())
for i in range(0, n):
    score = 0
    add = 0
    testcase = input()
    for j in range(0, len(testcase)):
        if testcase[j] == "O":
            add += 1
            score += add
        else:
            add = 0
    print(score)

# for i in range(0, n):
# ==
# for i in range(n):

# https://pacific-ocean.tistory.com/75
"""
a = int(input())
for i in range(a):
    b = input()
    s = list(b)
    sum = 0
    c = 1
    for i in s:
        if i == 'O':
            sum += c
            c += 1
        else:
            c = 1
    print(sum)
"""

# for i in s:
# i : item of list s
