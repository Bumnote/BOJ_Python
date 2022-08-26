from sys import stdin
from collections import deque

input = stdin.readline


def in_range(y, x):
    return 0 <= y < m and 0 <= x < n


def push(y, x):
    visited[y][x] = True
    q.append((y, x))


def bfs():
    cnt = 1
    dys, dxs = [-1, 1, 0, 0], [0, 0, -1, 1]
    while q:
        y, x = q.popleft()
        for dy, dx in zip(dys, dxs):
            new_y, new_x = y + dy, x + dx
            if in_range(new_y, new_x) and not visited[new_y][new_x] and grid[y][x] == grid[new_y][new_x]:
                cnt += 1
                push(new_y, new_x)
    # 탐색이 끝난다면, 사람의 수를 return
    return cnt


n, m = map(int, input().split())  # n: 가로 / m: 세로
grid = [list(input().strip()) for _ in range(m)]
visited = [[False for _ in range(n)] for _ in range(m)]
q = deque()
we = 0
other = 0

for y in range(m):
    for x in range(n):
        if not visited[y][x]:
            # 아군이라면 --> we 변수에 더해준다.
            if grid[y][x] == "W":
                push(y, x)
                we += (bfs() ** 2)
            # 적군이라면 --> other 변수에 더해준다.
            else:
                push(y, x)
                other += (bfs() ** 2)

print(f"{we} {other}")
