def solution(people, limit):
    people.sort()

    start = 0  # 정렬 후 제일 가벼운(맨 앞) 사람 인덱스
    end = len(people) - 1  # 정렬 후 제일 무거운(맨 뒤) 사람의 인덱스
    count = 0  # 필요한 보트의 수

    # 몸무게가 가장 큰 사람과 가장 작은 사람의 값을 더해 limit값과 비교한 다음,
    # 작으면 둘 다 태우고 크면 가장 큰 사람만 태운다
    while start <= end:
        count += 1
        if people[start] + people[end] <= limit:
            start += 1
        end -= 1

    return count
