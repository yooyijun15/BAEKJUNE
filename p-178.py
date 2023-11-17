N = int(input())
array = [int(input()) for _ in range(N)]

# 내림차순 정렬
array = sorted(array, reverse=True)

# 배열 출력
for i in array:
    print(i, end=' ')