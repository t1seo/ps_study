answers_1 = [1, 2, 3, 4, 5]
answers_2 = [1, 3, 2, 4, 2]


def solution(answers):
    result = []
    pattern1 = [1, 2, 3, 4, 5]
    pattern2 = [2, 1, 2, 3, 2, 4, 2, 5]
    pattern3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    score = [0, 0, 0]  # 학생별 정답 개수

    for idx, answer in enumerate(answers):  # enumerate
        if answer == pattern1[idx % len(pattern1)]:
            score[0] += 1
        if answer == pattern2[idx % len(pattern2)]:
            score[1] += 1
        if answer == pattern3[idx % len(pattern3)]:
            score[2] += 1

    for idx, s in enumerate(score):  # enumerate
        if s == max(score):
            result.append(idx + 1)

    return result

