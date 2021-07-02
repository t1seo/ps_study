answers_1 = [1, 2, 3, 4, 5]
answers_2 = [1, 3, 2, 4, 2]


def solution(answers):
    result = []  # 최종 리턴 리스트, 정답을 가장 많이 맞춘 학생의 번호 들어가게 된다

    # 수포자들의 정답 패턴
    student_1 = [1, 2, 3, 4, 5]
    student_2 = [2, 1, 2, 3, 2, 4, 2, 5]
    student_3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]

    # 수포자들이 정답 개수
    count_1 = 0
    count_2 = 0
    count_3 = 0

    for i in range(len(answers)):
        if answers[i] == student_1[i % 5]:  # 1번 학생의 패턴 길이가 5이므로 5씩 나눠준다
            count_1 += 1
        if answers[i] == student_2[i % 8]:  # 2번 학생
            count_2 += 1
        if answers[i] == student_3[i % 10]:  # 3번 학생
            count_3 += 1

    # 가장 정답을 많이 맞춘 횟수
    max_count = max(count_1, count_2, count_3)

    # 수포자들의 정답 개수와 가장 많이 맞춘 개수 비교 같으면 정답 리스트에 학생 추가
    if max_count == count_1:
        result.append(1)
    if max_count == count_2:
        result.append(2)
    if max_count == count_3:
        result.append(3)

    return result
