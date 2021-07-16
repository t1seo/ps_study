s_1 = "a234"
s_2 = "1234"


def solution(s):
    return s.isdigit() and len(s) == 4 or len(s) == 6


print(solution(s_1))
print(solution(s_2))
