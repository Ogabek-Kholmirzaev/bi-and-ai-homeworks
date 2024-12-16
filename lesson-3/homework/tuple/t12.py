tuple_nums = tuple(map(int, input().split()))

nums = sorted(tuple_nums)

if len(nums) > 1:
    print(nums[-2])