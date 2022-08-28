from sys import stdin
from collections import deque


def push(n, step):
    q.append((n, step))
    cnt[n] = step
    visited[n] = True


def bfs():
    while q:
        n, step = q.popleft()
        for elem in graph[n]:
            if not visited[elem]:
                push(elem, step + 1)


input = stdin.readline
vertex, edge = map(int, input().split())  # n: 정점 수 / m: 간선 수
graph = [[] for _ in range(vertex + 1)]
cnt = [0 for _ in range(vertex + 1)]
visited = [False for _ in range(vertex + 1)]

for _ in range(edge):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

q = deque()
push(1, 0)
bfs()

MAX = max(cnt)
print(f"{cnt.index(MAX)} {MAX} {cnt.count(MAX)}")
