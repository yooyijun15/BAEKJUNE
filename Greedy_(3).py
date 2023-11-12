# 1이 될 때까지
# 1) N에서 1을 뺀다.
# 2) N을 K로 나눈다. (단, 나누어 떨어질 때만 나눌 수 있다.)
# N을 1로 만들기 위해서 1)과 2) 실행 최소 횟수 구하기

N, K = map(int, input().split())
count = 0

while N > K:
    while N > 1:
        if N % K == 0:
           N = N//K
           count += 1
        else:
            N -= 1
            count += 1
        
print(count)