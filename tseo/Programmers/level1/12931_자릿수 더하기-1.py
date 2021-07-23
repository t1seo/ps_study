def solution(n):
    char_list = list(str(n))
    int_list = list(map(int, char_list))
    return sum(int_list)


print(solution(123))
print(solution(987))
