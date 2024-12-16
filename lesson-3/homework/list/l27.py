nums = list(map(int, input().split()))
first_index = int(input())
last_index = int(input())

if len(nums) == 0:
    print("empty list")
else:
    if last_index < first_index:
        print("first index is less than last index")
    else:
        sublist_nums = nums[first_index:last_index + 1]

        sublist_nums.sort()

        print(sublist_nums[-1])