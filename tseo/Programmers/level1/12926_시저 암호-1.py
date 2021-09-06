def solution(s, n):
    def converter(c, n):
        if c.islower():  # 소문자의 경우
            if ord(c) + n > ord("z"):  # 더한 숫자가 z보다 크면
                num = (ord(c) + n) - ord("z") - 1  # 한 바퀴 돌아서 a부터 얼마를 더해야 하는지 계산
                return chr(ord("a") + num)  # a부터 더하고 문자로 바꿔 리턴
            else:  # 더한 숫자가 z보다 작거나 같으면
                return chr(ord(c) + n)  # 그냥 숫자 더해주고 문자로 바꿔서 리턴
        elif c.isupper():  # 대문자의 경우
            if ord(c) + n > ord("Z"):
                num = (ord(c) + n) - ord("Z") - 1
                return chr(ord("A") + num)
            else:
                return chr(ord(c) + n)
        else:
            return c

    char_list = list(s)
    for i, c in enumerate(char_list):
        char_list[i] = converter(c, n)

    return "".join(char_list)


print(solution("AB", 1))
print(solution("z", 1))
print(solution("a B z", 4))
