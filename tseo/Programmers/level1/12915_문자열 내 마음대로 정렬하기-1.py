def solution(strings, n):
    # sorted_string = sorted(strings, key=lambda s: (s[n], s))
    return sorted(strings, key=lambda s: (s[n], s))


strings_1 = ["sun", "bed", "car"]
strings_2 = ["abce", "abcd", "cdx"]

print(solution(strings_1, 1))
print(solution(strings_2, 2))
