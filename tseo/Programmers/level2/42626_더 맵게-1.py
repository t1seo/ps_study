import heapq


def solution(scoville, k):
    heapq.heapify(scoville)  # scoville 리스트를 힙 구조로 만들어준다

    cnt = 0  # while 문 반복 횟수
    while scoville[0] < k:  # heap의 최소값이 k보다 커지면 break
        try:
            heapq.heappush(
                scoville, heapq.heappop(scoville) + (heapq.heappop(scoville) * 2)
            )
        except IndexError:  # 모든 음식의 스코빌 지수를 K 이상으로 만들 수 없는 경우
            return -1
        cnt += 1

    return cnt

