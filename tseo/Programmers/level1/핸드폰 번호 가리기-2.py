phone_number_1 = "01033334444"
phone_number_2 = "027778888"


def solution(s):
    return "*" * (len(s) - 4) + s[-4:]


print(solution(phone_number_1))
print(solution(phone_number_2))
