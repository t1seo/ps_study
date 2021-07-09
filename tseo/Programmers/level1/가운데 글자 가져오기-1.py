s1 = "abcde"
s2 = "qwer"


def solution(s):
    size = len(s)

    p = size // 2  # 중앙 위치
    if size % 2 == 0:  # 짝수라면
        pr = s[p]
        pl = s[p - 1]
        mid = pl + pr
    else:  # 홀수라면
        mid = s[p]

    return mid


print(solution(s1))
print(solution(s2))

