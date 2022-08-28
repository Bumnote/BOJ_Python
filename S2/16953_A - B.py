from sys import stdin
from collections import deque


def in_range(a):
    return a <= b


def push(a, cnt):
    q.append((a, cnt))


def bfs():
    while q:
        tmp, cnt = q.popleft()
        # b가 되었다면, 연산 횟수를 return
        if tmp == b:
            return cnt
        new_a = [tmp * 2, int(str(tmp) + "1")]
        for elem in new_a:
            # 범위를 벗어나지 않고, 방문한 적이 없던 숫자라면
            if in_range(elem):
                push(elem, cnt + 1)
    return -1


input = stdin.readline
# a -> b 로 바꾸기
a, b = map(int, input().split())

q = deque()
push(a, 1)

print(bfs())
