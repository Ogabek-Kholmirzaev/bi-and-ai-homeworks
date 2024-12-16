nums = list(map(int, input().split()))

cnt = 0

for num in nums:
    if num % 2 == 1:
        cnt += 1

print(cnt)