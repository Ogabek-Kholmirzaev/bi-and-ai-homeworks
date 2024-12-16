nums = list(map(int, input().split()))
old_element = int(input())
new_element = int(input())

if old_element in new_element:
    index = nums.index(old_element)
    nums[index] = new_element

print(nums)