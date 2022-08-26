from sys import stdin, setrecursionlimit

input = stdin.readline
setrecursionlimit(10 ** 6)


def in_range(y, x):
    return 0 <= y < n and 0 <= x < m


def dfs(y, x):
    visited[y][x] = True  # 방문 처리
    dys, dxs = [-1, -1, -1, 0, 1, 1, 1, 0], [-1, 0, 1, 1, 1, 0, -1, -1]
    for dy, dx in zip(dys, dxs):
        new_y, new_x = y + dy, x + dx
        if in_range(new_y, new_x) and not visited[new_y][new_x] and grid[new_y][new_x] == 1:
            dfs(new_y, new_x)


n, m = map(int, input().split())  # n: 행 / m: 열
grid = [list(map(int, input().split())) for _ in range(n)]
visited = [[False for _ in range(m)] for _ in range(n)]
word = 0

for y in range(n):
    for x in range(m):
        if not visited[y][x] and grid[y][x] == 1:
            dfs(y, x)
            word += 1

print(word)
