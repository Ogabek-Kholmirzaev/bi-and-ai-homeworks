nums = list(map(int, input().split()))
rotate = int(input())

if len(nums) > rotate:
    rotated_nums = nums[-rotate:] + nums[:-rotate]
    print(rotated_nums)