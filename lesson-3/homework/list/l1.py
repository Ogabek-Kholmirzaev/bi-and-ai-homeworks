arr = input().split()
element = input()

cnt = 0

for i in arr:
    if i == element:
        cnt += 1

print(cnt)