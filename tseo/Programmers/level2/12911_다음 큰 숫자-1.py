def solution(n):
    def count_one(n):
        count = 0
        for i in bin(n)[2:]:
            if i == "1":
                count += 1
        return count

    one_num = count_one(n)

    for i in range(n + 1, 1000001):
        if count_one(i) == one_num:
            return i


# count = 0
# for i in bin(78)[2:]:
#     if i == "1":
#         count += 1
# print(count)
# print(bin(78)[2:])
print(solution(78))
print(solution(15))
