from sys import stdin
input = stdin.readline # 입력 속도 증가

def dfs(pos):
    global answer
    visited[pos] = True  # 방문 처리

    for elem in graph[pos]:
        if not visited[elem]:  # 방문한 적이 없다면
            answer += 1  # 바이러스 걸린 컴퓨터 개수 증가
            dfs(elem)  # 연결된 다음 컴퓨터에서 깊이 탐색


vertex = int(input())  # 컴퓨터의 수 == 정점의 수
edge = int(input())  # 직접 연결된 컴퓨터 쌍의 수 == 간선의 수

graph = [[] for _ in range(vertex + 1)]
visited = [False for _ in range(vertex + 1)]

# 인접 행렬 입력
for _ in range(edge):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

answer = 0
dfs(1)

print(answer)
