prices = [1, 2, 3, 2, 3]


def solution(prices):
    answer = [0] * len(prices)

    for i in range(len(prices)):
        for j in range(i, len(prices) - 1):
            if prices[i] > prices[j]:  # i시점보다 낮은 가격의 price가 있으면
                break
            else:
                answer[i] += 1
    return answer


print(solution(prices))
