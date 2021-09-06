def solution(s):
    stack = []  # 빈 스택(여는 괄호만 쌓이게 된다)

    for i in s:
        if i == "(":  # 여는 괄호이면 스택에 push
            stack.append(i)
        else:  # 닫는 괄호이면
            if not stack:  # 스택이 비어있다면
                return False
            else:  # 스택에 있는 여는 괄호 제거
                stack.pop()

    return stack == []  # 다 돌았는데 스택이 비어있지 않다면 False
