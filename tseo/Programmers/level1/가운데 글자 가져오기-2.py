s1 = "abcde"
s2 = "qwer"


def solution(str):

    return str[(len(str) - 1) // 2 : len(str) // 2 + 1]


print(solution(s1))
print(solution(s2))

