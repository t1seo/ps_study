# https://programmers.co.kr/learn/courses/30/lessons/17680
# 2018 KAKAO BLIND RECRUITMENT > [1차] 캐시

def solution(cacheSize, cities):
    answer = 0
    cachebuc = []
    for i in range(len(cities)):
        cities[i] = cities[i].lower()
        if (len(cachebuc) != 0 and cities[i] in cachebuc):
            answer += 1
            ind = cachebuc.index(cities[i])
            cachebuc.pop(ind)		# LRU 알고리즘이므로 방금 쓴 건 항상 가장 마지막으로 업데이트
            cachebuc.append(cities[i])
        elif (cacheSize == 0): # 리스트가 항상 0인 경우 
            answer += 5
        elif (len(cachebuc) == cacheSize): # 리스트 maxlen일 때
            cachebuc.pop(0)
            cachebuc.append(cities[i])
            answer += 5
        else:					# 덜 찼을 때는 바로 추가 가능 
            cachebuc.append(cities[i])
            answer += 5
    return answer

"""모범코드
def solution(cacheSize, cities):
    import collections
    cache = collections.deque(maxlen=cacheSize)
"""