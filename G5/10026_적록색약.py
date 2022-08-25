from sys import stdin, setrecursionlimit

input = stdin.readline
setrecursionlimit(10 ** 6)


def in_range(y, x):
    return 0 <= y < n and 0 <= x < n


# 정상인의 경우 dfs 구현
def normal_dfs(y, x):
    visited[y][x] = True  # 방문 처리
    dys, dxs = [0, 0, -1, 1], [-1, 1, 0, 0]

    for dy, dx in zip(dys, dxs):
        new_y, new_x = y + dy, x + dx
        if in_range(new_y, new_x) and not visited[new_y][new_x] and grid[y][x] == grid[new_y][new_x]:
            normal_dfs(new_y, new_x)


# 적록색약인 경우 dfs 구현
def abnormal_dfs(y, x):
    visited[y][x] = True  # 방문 처리
    dys, dxs = [-1, 1, 0, 0], [0, 0, -1, 1]

    for dy, dx in zip(dys, dxs):
        new_y, new_x = y + dy, x + dx
        # grid의 현재 값이 R or G 인 경우
        if grid[y][x] == "R" or grid[y][x] == "G":
            if in_range(new_y, new_x) and not visited[new_y][new_x] and (
                    grid[new_y][new_x] == "R" or grid[new_y][new_x] == "G"):
                abnormal_dfs(new_y, new_x)
        # grid의 현재 값이 B 인 경우
        else:
            if in_range(new_y, new_x) and not visited[new_y][new_x] and grid[new_y][new_x] == "B":
                abnormal_dfs(new_y, new_x)


n = int(input())
# R: 빨강색 / G: 초록색 / B: 파랑색
# 적록색약 --> 빨강색과 초록색의 차이를 못 느껴 같게 본다.
grid = [list(input().strip()) for _ in range(n)]
a1, a2 = 0, 0

# 문제 해결
for t in range(2):
    tmp = grid
    visited = [[False for _ in range(n)] for _ in range(n)]
    # 정상인의 경우
    if t == 0:
        for y in range(n):
            for x in range(n):
                # 방문하지 않았다면,
                if not visited[y][x]:
                    normal_dfs(y, x)
                    a1 += 1 # dfs 탐색이 끝나면 값 증가
    # 적록색약인 경우
    else:
        for y in range(n):
            for x in range(n):
                # 방문하지 않았다면,
                if not visited[y][x]:
                    abnormal_dfs(y, x)
                    a2 += 1 # dfs 탐색이 끝나면 값 증가

print(a1, a2)
