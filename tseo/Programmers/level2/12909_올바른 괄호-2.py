def solution(s):
    x = 0
    for w in s:
        if x < 0:
            break
        x = x + 1 if w == "(" else x - 1 if w == ")" else x
    return x == 0

