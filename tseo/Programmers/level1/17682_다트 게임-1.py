def solution(dart_result):
    dart_list = list(dart_result)

    # dart 리스트에서 1, 0으로 되어 있는 점수를 10점으로 바꿔준다
    # ['1', 'D', '#', '2', 'S', '*', '3', 'S']
    # ['10', 'D', '#', '2', 'S', '*', '3', 'S']
    score_list = []
    for i in range(len(dart_result)):
        # 1을 만났을 떄 10인 경우
        if dart_list[i] == "1" and dart_list[i + 1] == "0":
            score_list.append("10")
        # 0을 만났을 때 10이면 중복이므로 continue
        elif dart_list[i] == "0" and dart_list[i - 1] == "1":
            continue
        else:
            score_list.append(dart_list[i])

    answer = []
    for i in range(1, len(score_list)):
        if score_list[i] == "S":
            answer.append(int(score_list[i - 1]))
        elif score_list[i] == "D":  # double
            answer.append(int(score_list[i - 1]) ** 2)
        elif score_list[i] == "T":  # triple
            answer.append(int(score_list[i - 1]) ** 3)

        # 옵션: 스타상과 아차상
        if score_list[i] == "*":  # 스타상
            if len(answer) >= 2:  # 스코어를 2개 이상 구해놓았다면
                answer[-1] = answer[-1] * 2
                answer[-2] = answer[-2] * 2
            else:
                answer[-1] = answer[-1] * 2  # 스코어를 1개 구해놓았다면
        elif score_list[i] == "#":  # 아차상
            answer[-1] = answer[-1] * -1  # 해당 점수만 -1배

    return sum(answer)


dr_1 = "1S2D*3T"
dr_2 = "1D2S#10S"
dr_3 = "1D2S0T"
dr_4 = "1S*2T*3S"
dr_5 = "1D#2S*3S"
dr_6 = "1T2D3D#"
dr_7 = "1D2S3T*"

print(solution(dr_1))
print(solution(dr_2))
print(solution(dr_3))
print(solution(dr_4))
print(solution(dr_5))
print(solution(dr_6))
print(solution(dr_7))
