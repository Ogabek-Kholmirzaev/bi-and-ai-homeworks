nums = list(map(int, input().split()))

unique_nums = []

for i in nums:
    cnt = 0

    for j in nums:
        if i == j:
            cnt += 1

    if cnt == 1:
        unique_nums.append(i)

print(unique_nums)