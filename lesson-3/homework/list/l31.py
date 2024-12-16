nums = list(map(int, input().split()))
repeat_count = int(input())

new_nums = []

for i in range(len(nums)):
    cnt = 0

    for j in range(repeat_count):
        if nums[i] == nums[j]:
            cnt += 1

    if cnt == repeat_count:
        new_nums.append(nums[i])

print(new_nums)