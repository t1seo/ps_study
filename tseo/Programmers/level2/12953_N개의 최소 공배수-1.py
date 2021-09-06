from math import gcd


def solution(arr):
    def lcm(x, y):
        return x * y // gcd(x, y)

    while True:
        arr.append(lcm(arr.pop(), arr.pop()))
        if len(arr) == 1:
            return arr[0]


arr_1 = [2, 6, 8, 14]
arr_2 = [1, 2, 3]

print(solution(arr_1))
print(solution(arr_2))
