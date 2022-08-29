from sys import stdin, maxsize

input = stdin.readline


def check(heights, height, b):
    time = 0  # 걸리는 시간
    cnt = 0  # 채워 넣어야할 블록 개수

    for y in range(n):
        for x in range(m):
            tmp = heights[y][x] - height
            if tmp > 0:  # level 보다 높다면 --> 잘라내야 한다.
                b += tmp  # 인벤토리에 저장 --> 2초
                time += 2 * tmp  # 2초 증가
            else:  # 높지 않다면 -- > 채워 넣어야 한다. --> 1초 경과
                cnt += -tmp
    # 채워 넣어야할 블록보다 인벤토리에 저장된 블록이 적다면 --> 불가능
    if b < cnt:
        return maxsize
    # 채워 넣어야할 블록만큼 인벤토리에 저장되어있다면 --> 가능
    return time + cnt


n, m, b = map(int, input().split())  # n: 행 / m: 열 / b: 인벤토리에 들어있는 블록 개수
heights = [list(map(int, input().split())) for _ in range(n)]

# 땅 고르기 작업 실행
# 블록 제거 후 인벤토리 저장 -> 2초
# 인벤토리에서 블록 꺼내서 쌓기 -> 1초
MIN = min([min(elem) for elem in heights])  # 가장 낮은 높이
MAX = max([max(elem) for elem in heights])  # 가장 높은 높이

min_time = maxsize
min_level = 0
for height in range(MAX, MIN - 1, - 1):
    time = check(heights, height, b)
    if min_time > time:
        min_time = time
        min_level = height

print(f"{min_time} {min_level}")
