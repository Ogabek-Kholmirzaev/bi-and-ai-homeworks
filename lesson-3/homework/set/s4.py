set1 = set(map(int, input().split()))
set2 = set(map(int, input().split()))

is_subset = set1.issubset(set2)

print(is_subset)