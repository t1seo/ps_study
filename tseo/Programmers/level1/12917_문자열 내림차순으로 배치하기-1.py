def solution(s):
    str_list = sorted(s)
    # str_list = sorted(str_list, reverse=True)

    return "".join(str_list)


print(solution("Zbcdefg"))
