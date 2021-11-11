import heapq 

""" 힙이란? 최댓값과 최솟값을 빠르게 찾기 위해 고안된 자료구조 
heap = []
heapq.heappush(heap, 1)
heapq.heappop(heap) 가장 작은 원소를 리턴 
heapq.heappify([7,5,8,3]) 기존 집합을 heapify 
heap[0] 삭제하지 않고 최솟값 접근 
heapq.heappush(heap, (-num, num)) 최대힙 
"""

def dijkstra(distance, adj):
    heap = []
    heapq.heappush(heap, [0, 1])
    # cost 0 첫번째 마을에서 시작 

    while heap:
        cost, node = heapq.heappop(heap)
        for c, n in adj[node]:
            if cost+c < distance[n]: # inf였던 max값을 업데이트
                distance[n] = cost + c
                heapq.heappush(heap, [cost+c, n])
    """ 
    끝나면 cost가 작은 순서대로 나와 distance를 업데이트한다 
    그러면 해당 마을마다 첫번째 마을에서 거기까지 도달할 때까지 distance가 나온다 
    """

def solution(n, road, k): # 마을개수, road배열, 시간
    maxx = float('inf')
    distance = [maxx]*(n+1)
    distance[1] = 0 # 마을 1초기화 
    print(distance) # [inf, 0, inf, inf, inf, inf]
    adj = [[] for _ in range(n+1)]
    print(adj) # [[], [], [], [], [], []]
    
    for r in road:
        adj[r[0]].append([r[2], r[1]])
        adj[r[1]].append([r[2], r[0]])
    """
    r[0]은 출발하는 마을, r[1]은 도착하는 마을이다. 
    adj 마을 인덱스마다 []로 시작. 순서대로 두 값을 넣을 건데 
    adj[r[0]] 출발하는 마을의 배열에는 [거리, 도착마을 ]
    adj[r[1]] 도착하는 마을의 배열에는 [거리, 출발마을 ]
    **결국 adj은 인덱스는 출발하는 쪽, adj[ind][1]은 도착하는 쪽이 저장된다. 

    마을마다 다리가 여러개 있을 수 있기 때문에 자기와 연결된 다리만큼 각 마을에 생길 예정 
    예를 들어 1번마을에 연결하는 도로는 두 개니까 [거리1, 2번마을], [거리2, 4번마을]이 들어간다 
    다 정리된 이중배열 adj는 다익스트라 알고리즘에서 쓰인다
    print(adj)
    [[], [[1, 2], [2, 4]], [[1, 1], [3, 3], [2, 5]], \
    [[3, 2], [1, 5]], [[2, 1], [2, 5]], [[2, 2], [1, 3], [2, 4]]]
    """
    
    dijkstra(distance, adj)
    return len([x for x in distance if x <= k])

# a = solution(5, [[1,2,1],[2,3,3],[5,2,2],[1,4,2],[5,3,1],[5,4,2]], 3)
# print(a)