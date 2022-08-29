from sys import stdin

k , n = map(int, input().split()) # k: 이미 가지고 있는 랜선의 개수 / n: 필요한 랜선의 개수
# k 개의 랜선은 모두 제각각 / 이미 자른 랜선은 붙일 수 없다.
length = [ int(input()) for _ in range(k)] # k 개의 랜선의 길이 입력

low = 1 # 가장 낮은 값
high = max(length) # 가장 높은 값
# 이진 탐색 구현
while low < high:
    mid = ((low + high)// 2) + 1
    answer = sum([LEN // mid for LEN in length ]) # 해당 길이만큼 몇 개의 랜선을 만들 수 있는 지 확인
    if answer >= n:
        low = mid
    else:
        high = mid - 1

print(low)