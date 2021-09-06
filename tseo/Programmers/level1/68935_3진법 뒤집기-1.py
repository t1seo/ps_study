def solution(n):

    # 3진법 리스트를 만들어준다 (역순)
    l = []
    while n > 0:
        l.append(n % 3)
        n //= 3

    # 리스트 원소를 하나씩 빼주면서 10진법으로 계산
    result = 0
    i = 0
    while l:
        num = l.pop()
        result += num * (3 ** i)
        i += 1

    return result


print(solution(45))
print(solution(125))
