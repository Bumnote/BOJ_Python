from sys import stdin
from collections import deque

input = stdin.readline


def in_range(y, x):
    return 0 <= y < n and 0 <= x < n


def push(y, x, step):
    visited[y][x] = True  # 방문 처리
    q.append((y, x, step))


def bfs():
    dys, dxs = [-2, -2, 0, 0, 2, 2], [-1, 1, -2, 2, -1, 1]

    while q:
        y, x, step = q.popleft()
        if y == r2 and x == c2:
            return step
        for dy, dx in zip(dys, dxs):
            new_y, new_x = y + dy, x + dx
            if in_range(new_y, new_x) and not visited[new_y][new_x]:
                push(new_y, new_x, step + 1)
    # while 문을 탈출했다는 건 (r2, c2) 위치로 이동할 수 없다는 뜻이기 때문에, -1을 return
    return -1


n = int(input().strip())
grid = [[0 for _ in range(n)] for _ in range(n)]
visited = [[False for _ in range(n)] for _ in range(n)]
# (r1, c1) ---> (r2, c2) 이동
r1, c1, r2, c2 = map(int, input().split())

q = deque()
push(r1, c1, 0)

print(bfs())
