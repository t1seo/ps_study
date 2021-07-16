s_1 = "a234"
s_2 = "1234"


def solution(s):
    return s.isdigit() and len(s) in (4, 6)


print(solution(s_1))
print(solution(s_2))
