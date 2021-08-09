def solution(nums):
    return min(len(nums) / 2, len(set(nums)))


n1 = [3, 3, 3, 2, 2, 4]
n2 = [3, 3, 3, 2, 2, 2]
print(solution(n2))
