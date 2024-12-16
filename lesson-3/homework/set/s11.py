set1 = set(map(int, input().split()))
set2 = set(map(int, input().split()))

symmetric_difference_set = set1 ^ set2

print(symmetric_difference_set)
