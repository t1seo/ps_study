from itertools import combinations


def solution(number, k):
    combi = combinations(list(number), len(number) - k)  # k개를 제외한 조합을 만들어준다
    combi = list(combi)

    numbers = []
    for num in combi:
        numbers.append(int("".join(num)))  # 숫자들을 합쳐준다

    return str(max(numbers))  # 최대값을 찾은 후 str로 변환하고 리턴


number_1 = "1924"
number_2 = "1231234"
number_3 = "4177252841"

print(solution(number_1, 2))
print(solution(number_2, 3))
print(solution(number_3, 4))
