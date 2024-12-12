s = input()
res = False

for char in s:
    if (char.isdigit()):
        res = True
        break

print(res)