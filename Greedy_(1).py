# 큰 수의 법칙 응용
# N개의 숫자를 입력 받은 뒤, 입력 받은 숫자를 M번 더하여 가장 큰 숫자를 만드는 문제
# (단, K번째 숫자는 연속으로 3번까지 밖에 올 수 없다.)

N, M, K = map(int, input().split())
# numbers_list = [int(input()) for _ in range(N)] # Enter로 구분
numbers_list = list(map(int, input().split())) # Space로 구분

sum = 0
a = 0
b = 0

A = numbers_list[K-1]
numbers_list.sort()

if numbers_list[N-1] == A:
    a += M//4
    b += M%4
    sum = (numbers_list[N-1]*3 + numbers_list[N-2])*a + (numbers_list[N-1])*b
else:
    sum = numbers_list[N-1]*M

print(sum)