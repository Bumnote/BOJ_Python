from sys import stdin
from collections import deque

input = stdin.readline


def in_range(x):
    return 1 <= x <= 100


def push(pos, step):
    q.append((pos, step))  # deque에 저장
    visited[pos] = True  # 방문 처리


def bfs():
    move = [1, 2, 3, 4, 5, 6]

    while q:
        pos, step = q.popleft()

        for elem in move:
            new_pos = pos + elem
            # 만약 새롭게 이동한 칸이 사다리 혹은 뱀이 있는 곳이라면 (중복 X)
            if new_pos in ladder:
                new_pos = ladder[new_pos]  # 사다리 타고 이동
            if new_pos in snake:
                new_pos = snake[new_pos]  # 뱀타고 이동
            if new_pos == 100:  # 목표 지점까지 도달했다면
                return step + 1  # 한칸 이동한 후 return

            if in_range(new_pos) and not visited[new_pos]:
                push(new_pos, step + 1)


# 게임의 목표 1번 칸에서 시작해서 100번칸 까지 도착하는 것
n, m = map(int, input().split())  # n: 사다리의 수 / m: 뱀의 수

# 판
grid = [num for num in range(101)]
visited = [False for _ in range(101)]
# 사다리와 뱀의 정보 dictionary로 입력
ladder = {}
snake = {}

for _ in range(n):
    x, y = map(int, input().split())
    ladder[x] = y

for _ in range(m):
    u, v = map(int, input().split())
    snake[u] = v

q = deque()
push(1, 0)

answer = bfs()
print(answer)
