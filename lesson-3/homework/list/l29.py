nums = list(map(int, input().split()))
element = int(input())

removed_nums = [num for num in nums if num != element]

print(removed_nums)