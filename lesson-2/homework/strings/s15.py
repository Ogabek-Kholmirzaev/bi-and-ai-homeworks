s = input()

res = ""

words = s.split(' ')

for word in words:
    res += word[0]

print(res)