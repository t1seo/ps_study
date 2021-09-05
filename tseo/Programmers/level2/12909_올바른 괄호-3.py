def solution(s):
    st = list()
    for c in s:
        if c == "(":
            st.append(c)

        if c == ")":
            try:
                st.pop()
            except IndexError:
                return False

    return len(st) == 0
