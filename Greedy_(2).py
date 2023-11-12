# 큰 수의 법칙
# N개의 숫자를 입력 받은 뒤, 입력 받은 숫자를 M번 더하여 가장 큰 숫자를 만드는 문제
# (단, 모든 숫자는 연속으로 K번까지 밖에 쓸 수 없다.)

N, M, K = map(int, input().split())
numbers_list = list(map(int, input().split()))

numbers_list.sort()

Frist = numbers_list[N-1]
Second = numbers_list[N-2]

sum = 0
a = 0
b = 0

if Frist == Second:
    sum = Frist * M
else:
    a += M//(K+1)
    b += M % (K+1)
    sum = (Frist*K + Second)*a + (Frist*b)

print(sum)