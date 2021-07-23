def solution(s):
    def converter(word):
        """
        한 단어를 다음과 같이 바꿔준다
            짝수->대문자
            홀수->소문자
        """
        char_list = list(word)
        for i, c in enumerate(char_list):
            if i % 2 == 0:
                char_list[i] = c.upper()
            else:
                char_list[i] = c.lower()
        return "".join(char_list)

    words = s.split(" ")
    # result = []
    result = list(map(converter, words))

    # for word in words:
    #     result.append(converter(word))

    return " ".join(result)


print(solution("try hello world"))
