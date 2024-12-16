nums = tuple(map(int, input().split()))
element = int(input())

cnt = 0

for num in nums:
    if num == element:
        cnt += 1

print(cnt)