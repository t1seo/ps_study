def solution(absolutes, signs):
    result = 0

    for num, sign in zip(absolutes, signs):
        if sign:
            result += num
        else:
            result -= num

    return result

