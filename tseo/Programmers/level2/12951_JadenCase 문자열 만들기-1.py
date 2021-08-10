def solution(s):
    word_list = s.split(" ")
    for i in range(len(word_list)):
        word_list[i] = word_list[i].capitalize()
    return " ".join(word_list)


s_1 = "3people unFollowed me"
s_2 = "for the last week"

print(solution(s_1))
print(solution(s_2))

