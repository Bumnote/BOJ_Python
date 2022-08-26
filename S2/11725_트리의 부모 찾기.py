from sys import stdin, setrecursionlimit

input = stdin.readline
setrecursionlimit(10 ** 6)


def dfs(n):
    visited[n] = True  # 방문 처리

    for elem in graph[n]:
        if not visited[elem]:
            parent_node[elem] = n  # 부모의 노드를 저장
            dfs(elem)


vertex = int(input().strip())  # 노드의 개수
graph = [[] for _ in range(vertex + 1)]  # 그래프 구현
visited = [False for _ in range(vertex + 1)]  # 방문 여부 확인
parent_node = [0 for _ in range(vertex + 1)]  # 부모 노드 확인

# 간선 입력
for _ in range(vertex - 1):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

# 연결 정보 오름차순 정렬
for elem in graph:
    elem.sort()

dfs(1)  # dfs(부모)

for elem in parent_node[2:]:
    print(elem)
