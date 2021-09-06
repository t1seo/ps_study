import re


def solution(dartResult):
    bonus = {"S": 1, "D": 2, "T": 3}
    option = {"": 1, "*": 2, "#": -1}

    p = re.compile("(\d+)([SDT])([*#]?)")
    dart = p.findall(dartResult)

    print(dart)

    for i in range(len(dart)):
        if dart[i][2] == "*" and i > 0:
            dart[i - 1] *= 2
        dart[i] = int(dart[i][0]) ** bonus[dart[i][1]] * option[dart[i][2]]

    answer = sum(dart)
    return answer


dr_1 = "1S2D*3T"
dr_2 = "1D2S#10S"
# dr_3 = "1D2S0T"
# dr_4 = "1S*2T*3S"
# dr_5 = "1D#2S*3S"
# dr_6 = "1T2D3D#"
# dr_7 = "1D2S3T*"

# print(solution(dr_1))
print(solution(dr_2))
# print(solution(dr_3))
# print(solution(dr_4))
# print(solution(dr_5))
# print(solution(dr_6))
# print(solution(dr_7))
