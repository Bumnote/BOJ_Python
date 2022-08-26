from sys import stdin, setrecursionlimit

input = stdin.readline
setrecursionlimit(10 ** 6)


def in_range(y, x):
    return 0 <= y < n and 0 <= x < m


def dfs(y, x):
    global answer
    visited[y][x] = True  # 방문 처리
    # 끝에 도달했다면 --> return True
    if y == n - 1:
        answer = 1
    dys, dxs = [-1, 1, 0, 0], [0, 0, -1, 1]
    for dy, dx in zip(dys, dxs):
        new_y, new_x = y + dy, x + dx
        if in_range(new_y, new_x) and not visited[new_y][new_x] and grid[new_y][new_x] == 0:
            dfs(new_y, new_x)
    # 끝에 도달하지 못했다면 --> return False



n, m = map(int, input().split())
# 0: 전류가 통한다. / 1: 전류가 통하지 않는다.
grid = [list(map(int, input().strip())) for _ in range(n)]
visited = [[False for _ in range(m)] for _ in range(n)]
answer = 0

for i in range(m):
    if not visited[0][i] and grid[0][i] == 0:
        dfs(0, i)

print("YES" if answer == 1 else "NO")
