from sys import stdin

input = stdin.readline

n, m = map(int, input().split())  # n: 나무의 수 / m: 가져가려고 하는 나무의 길이
tree = list(map(int, input().split()))
low = 0  # 나무의 최저 높이
high = max(tree)  # 나무의 최대 높이 

# 이진 탐색 구현
while low < high:
    mid = (low + high) // 2 + 1
    Sum = sum([max(0, elem - mid) for elem in tree])
    if Sum >= m:
        low = mid
    else:
        high = mid - 1

print(low)
