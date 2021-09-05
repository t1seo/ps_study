def is_pair(s):
    # 함수를 완성하세요
    x = 0
    for w in s:
        if x < 0:
            break
        x = x + 1 if w == "(" else x - 1 if w == ")" else x
    return x == 0

