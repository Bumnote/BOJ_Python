from sys import stdin
from collections import deque
# "3187_양"과 같은 문제
input = stdin.readline


def in_range(y, x):
    return 0 <= y < r and 0 <= x < c


def push(y, x):
    visited[y][x] = True
    q.append((y, x))


def bfs():
    sheep = 0
    wolf = 0
    dys, dxs = [-1, 1, 0, 0], [0, 0, -1, 1]
    while q:
        y, x = q.popleft()
        if grid[y][x] == "v":
            wolf += 1
        if grid[y][x] == "k":
            sheep += 1
        for dy, dx in zip(dys, dxs):
            new_y, new_x = y + dy, x + dx
            if in_range(new_y, new_x) and not visited[new_y][new_x] and grid[new_y][new_x] != "#":
                push(new_y, new_x)

    if sheep == 0 and wolf == 0:
        return (0, 0)
    elif sheep > wolf:
        return (sheep, 0)
    else:
        return (0, wolf)


r, c = map(int, input().split())  # r: 행 / c: 열
grid = [list(input().strip()) for _ in range(r)]
visited = [[False for _ in range(c)] for _ in range(r)]

q = deque()
answer_sheep = 0
answer_wolf = 0
for y in range(r):
    for x in range(c):
        if not visited[y][x] and grid[y][x] != "#":
            push(y, x)
            sheep, wolf = bfs()
            answer_sheep += sheep
            answer_wolf += wolf

print(f"{answer_sheep} {answer_wolf}")
