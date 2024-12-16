tuple_nums = tuple(map(int, input().split()))
first_index = int(input())
last_index = int(input())

if first_index > last_index:
    print("null")
else:
    nums = tuple_nums[first_index:last_index + 1]

    print(sorted(nums)[0])