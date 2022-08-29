from sys import stdin
from collections import deque

input = stdin.readline


def in_range(a_x, a_y, b_x, b_y):
    return abs(b_x - a_x) + abs(b_y - a_y)


def bfs():
    while q:
        x, y = q.popleft()
        if in_range(x, y, festival_x, festival_y) <= 1000:
            print("happy")
            return
        for i in range(store_cnt):
            store_x, store_y = store[i]
            # 방문한 적이 없다면
            if (store_x, store_y) not in visited:
                if in_range(x, y, store_x, store_y) <= 1000:
                    visited.append((store_x, store_y))
                    q.append((store_x, store_y))

    print("sad")
    return


tc = int(input().strip())
for _ in range(tc):
    q = deque()
    visited = deque()
    store_cnt = int(input().strip())
    start_x, start_y = map(int, input().split())
    q.append((start_x, start_y))
    # 맥주 20병 / 병 당 50m 이동 가능
    store = [tuple(list(map(int, input().split()))) for _ in range(store_cnt)]
    festival_x, festival_y = map(int, input().split())
    bfs()
