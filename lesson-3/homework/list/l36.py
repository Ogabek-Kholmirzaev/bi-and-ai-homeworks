nums = list(map(int, input().split()))

sum = 0

for num in nums:
    if num > 0:
        sum += num

print(sum)