nums = list(map(int, input().split()))

if nums == nums[::-1]:
    print(True)
else:
    print(False)