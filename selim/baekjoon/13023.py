import sys 
input = sys.stdin.readline

n, m = map(int, input().split())
graph = [[] for i in range(n)]
for i in range(m):
    a, b = (list(map(int,input().split())))
    graph[a].append(b)
    graph[b].append(a)
# print(graph)

# visited = [0 for i in range(n)]
answer = [0]
def dfs(lev, visited, st): 
    # print(visited)
    if lev == 4 : 
        # print(visited)
        answer[0] = 1
        return 
    for i in graph[st]: 
        if visited[i] == 0: 
            visited[i] = 1
            dfs(lev+1, visited, i)
            visited[i] = 0
        if answer[0] == 1 : 
            return 
    
for i in range(n): 
    visited = [0 for i in range(n)]
    visited[i] = 1
    dfs(0, visited, i)
print(answer[0])

"""
6 5
0 1
1 2
2 3
1 4
4 5
"""
