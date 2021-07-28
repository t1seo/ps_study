def solution(arr, divisor):
    return sorted([n for n in arr if n % divisor == 0]) or [-1]


arr = [2, 36, 1, 3]
divisor = 11

print(solution(arr, divisor))
