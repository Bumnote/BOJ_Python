from sys import stdin, setrecursionlimit

input = stdin.readline
setrecursionlimit(10 ** 6)


def in_range(y, x):
    return 0 <= y < n and 0 <= x < m


def dfs(y, x):
    global cnt
    visited[y][x] = True  # 방문 처리

    dys, dxs = [-1, 1, 0, 0], [0, 0, -1, 1]  # dy, dx 테크닉
    for dy, dx in zip(dys, dxs):
        new_y, new_x = y + dy, x + dx
        if in_range(new_y, new_x) and not visited[new_y][new_x] and grid[new_y][new_x] == "#":
            cnt += 1
            dfs(new_y, new_x)


n, m, k = map(int, input().split())

grid = [["-" for _ in range(m)] for _ in range(n)]
visited = [[False for _ in range(m)] for _ in range(n)]
for _ in range(k):
    r, c = map(int, input().split())
    grid[r - 1][c - 1] = "#"

max_trash = 0
for y in range(n):
    for x in range(m):
        if grid[y][x] == "#":
            cnt = 1  # 쓰레기의 개수를 계속 초기화
            dfs(y, x)
            max_trash = max(cnt, max_trash)  # 쓰레기의 최댓값을 갱신

print(max_trash)
