phone_number_1 = "01033334444"
phone_number_2 = "027778888"


def solution(phone_number):
    a = phone_number[:-4]  # 맨앞부터 4자리 전까지
    b = phone_number[-4:]  # 맨 끝 4자리

    return len(a) * "*" + b


print(solution(phone_number_1))
print(solution(phone_number_2))
