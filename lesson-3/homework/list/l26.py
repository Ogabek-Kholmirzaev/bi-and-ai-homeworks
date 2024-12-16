nums = list(map(int, input().split()))

if len(nums) % 2 == 1:
    print(nums[len(nums) // 2])
else:
    print(f"{nums[len(nums) // 2 - 1]}, {nums[len(nums) // 2]}")