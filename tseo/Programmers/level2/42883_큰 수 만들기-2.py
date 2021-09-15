def solution(number, k):
    stack = [number[0]]  # 스택에 맨 앞의 숫자를 넣어준다

    for num in number[1:]:  # number에서 두 번째 숫자부터
        while len(stack) > 0 and stack[-1] < num and k > 0:
            k -= 1  # 스택에서 값을 뺄 때마다 k에서 1을 뺴준다. 값을 제거해주는 거니까
            stack.pop()  # num보다 스택의 맨 뒤의 숫자가 작으면 pop을 해준다.
        stack.append(num)  # 스택에 있는 숫자가 더 크다면 num을 스택에 넣어준다

    # k가 0이 아니라면 덜 제거 했으므로 슬라이싱 해준다
    if k != 0:
        stack = stack[:-k]
    return "".join(stack)


# number_1 = "1924"
# number_2 = "1231234"
number_3 = "4177252841"

# print(solution(number_1, 2))
# print(solution(number_2, 3))
# print(solution(number_3, 4))


print(number_3[:-2])
