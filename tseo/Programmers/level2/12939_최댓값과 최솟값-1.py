def solution(s):
    s = s.split(" ")
    s = list(map(int, s))
    a = str(min(s))
    b = str(max(s))
    return a + " " + b


print(solution("1 2 3 4"))
