a = 5
b = 24

DAY_OF_THE_WEEK = ["FRI", "SAT", "SUN", "MON", "TUE", "WED", "THU"]  # 요일
DAYS_OF_THE_MONTH = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]  # 각 월의 일 수


def solution(a, b):
    days = 0  # a월 전까지의 총 날짜
    for i in range(a - 1):
        days += DAYS_OF_THE_MONTH[i]

    days += b  # 해당 월의 날짜 더해주기
    idx = days % 7 - 1
    return DAY_OF_THE_WEEK[idx]


print(solution(a, b))

