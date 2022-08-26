from sys import stdin
from collections import deque

input = stdin.readline


def in_range(y, x):
    return 0 <= y < n and 0 <= x < m


def push(y, x):
    q.append((y, x))
    visited[y][x] = True


def bfs():
    global cnt
    dys, dxs = [-1, 1, 0, 0], [0, 0, -1, 1]
    while q:
        y, x = q.popleft()

        for dy, dx in zip(dys, dxs):
            new_y, new_x = y + dy, x + dx
            # 범위를 벗어나지 않고, 방문하지 않았고, 그림이 존재한다면
            if in_range(new_y, new_x) and not visited[new_y][new_x] and grid[new_y][new_x] == 1:
                cnt += 1
                push(new_y, new_x)


n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]
visited = [[False for _ in range(m)] for _ in range(n)]
picture = []
q = deque()

for y in range(n):
    for x in range(m):
        if not visited[y][x] and grid[y][x] == 1:
            cnt = 1
            push(y, x)
            bfs()
            picture.append(cnt)  # 탐색한 개수를 append

if len(picture) != 0:
    print(f"{len(picture)}\n{max(picture)}")  # 원소의 개수 = 그림의 개수 / 원소의 최댓값 = 그림의 최대 넓이
else:
    print(f"{0}\n{0}")
