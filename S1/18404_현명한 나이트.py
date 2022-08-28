from sys import stdin
from collections import deque

input = stdin.readline


def in_range(y, x):
    return 0 <= y < n and 0 <= x < n


def push(y, x, step):
    q.append((y, x, step))
    visited[y][x] = True  # 방문 처리


def bfs():
    dys, dxs = [-1, -2, -2, -1, 1, 2, 2, 1], [-2, -1, 1, 2, 2, 1, -1, -2]
    while q:
        y, x, step = q.popleft()
        if grid[y][x] == "H":
            answer[pos.index([y, x])] = step
        for dy, dx in zip(dys, dxs):
            new_y, new_x = y + dy, x + dx
            if in_range(new_y, new_x) and not visited[new_y][new_x]:
                push(new_y, new_x, step + 1)


n, m = map(int, input().split())
# 체스 판 구현
grid = [[0 for _ in range(n)] for _ in range(n)]
r, c = map(int, input().split())
visited = [[False for _ in range(n)] for _ in range(n)]
# 말의 위치를 순서대로 담아둔다.
pos = []
for _ in range(m):
    u, v = map(int, input().split())
    pos.append([u - 1, v - 1])
# 말 모양 표시
for elem in pos:
    grid[elem[0]][elem[1]] = "H"
# BFS로 풀이
q = deque()
answer = [0] * m
push(r - 1, c - 1, 0)
bfs()

# 정답 출력
for elem in answer:
    print(elem, end=" ")
