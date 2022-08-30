from sys import stdin
input = stdin.readline

# n개의 숫자 중에서 m 개를 뽑는 조합 구현
def simulate(curr_num, cnt):
    if curr_num == n:
        if cnt == m:
            for i in range(n):
                if arr[i] == 1:
                    print(i+1,end=" ")
            print()
        return

    arr.append(1)
    simulate(curr_num + 1, cnt + 1)
    arr.pop()

    arr.append(0)
    simulate(curr_num + 1, cnt)
    arr.pop()

n, m = map(int, input().split())
arr = []
simulate(0, 0)